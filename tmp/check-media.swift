import Foundation
import AVFoundation
import AppKit
let root = URL(fileURLWithPath: CommandLine.arguments[1])
for name in ["oud-story", "banana-matcha", "matcha-moments"] {
  let asset = AVURLAsset(url: root.appendingPathComponent("assets/\(name).mp4"))
  print(name, "duration", CMTimeGetSeconds(asset.duration), "playable", asset.isPlayable, "tracks", asset.tracks.count)
  let generator = AVAssetImageGenerator(asset: asset)
  generator.appliesPreferredTrackTransform = true
  do {
    let cg = try generator.copyCGImage(at: CMTime(seconds: 1, preferredTimescale: 600), actualTime: nil)
    let bitmap = NSBitmapImageRep(cgImage: cg)
    let data = bitmap.representation(using: .jpeg, properties: [.compressionFactor: 0.85])!
    try data.write(to: root.appendingPathComponent("assets/original/\(name)-poster.jpg"))
    print("decoded", cg.width, cg.height)
  } catch { print("DECODE FAILED", error) }
}
