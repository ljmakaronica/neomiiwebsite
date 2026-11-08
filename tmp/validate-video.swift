import Foundation
import JavaScriptCore
let context = JSContext()!
var failed = false
context.exceptionHandler = { _, exception in
  failed = true
  print("FAIL:", exception?.toString() ?? "Unknown JavaScript error")
}
context.evaluateScript("""
var motion = { matches: false, addEventListener: function(type, handler) { this.handler = handler; } };
var window = { matchMedia: function() { return motion; }, IntersectionObserver: true };
function fakeVideo(end) {
  return {
    dataset: end ? {end: String(end)} : {}, paused: true, ended: false,
    currentTime: 0, playCount: 0, handlers: {},
    addEventListener: function(name, fn) { (this.handlers[name] ||= []).push(fn); },
    emit: function(name) { (this.handlers[name] || []).forEach(fn => fn()); },
    play: function() { this.paused = false; this.playCount++; this.emit('play'); return Promise.resolve(); },
    pause: function() { this.paused = true; this.emit('pause'); }
  };
}
var reels = [fakeVideo(), fakeVideo(), fakeVideo(11.21)];
var document = { querySelectorAll: function() { return reels; } };
var visibility;
function IntersectionObserver(fn) { visibility = fn; this.observe = function() {}; }
function assert(value, message) { if (!value) throw Error(message); }
function visible(video, value) { visibility([{target: video, isIntersecting: value}]); }
""")
let source = try String(contentsOfFile: CommandLine.arguments[1], encoding: .utf8)
context.evaluateScript(source)
context.evaluateScript("""
visible(reels[0], true);
assert(reels[0].playCount === 1, 'Visible video should play');
reels[0].pause();
visible(reels[0], false); visible(reels[0], true);
assert(reels[0].playCount === 1, 'Explicit user pause must be preserved');
visible(reels[1], true); visible(reels[1], false); visible(reels[1], true);
assert(reels[1].playCount === 2, 'Offscreen pause should allow automatic resumption');
visible(reels[2], true); reels[2].currentTime = 11.3; reels[2].emit('timeupdate');
assert(reels[2].currentTime === 0, 'Published clip end must loop to the beginning');
motion.matches = true; motion.handler({matches: true});
assert(reels.every(video => video.paused), 'Reduced motion should stop automatic playback');
visible(reels[1], false); visible(reels[1], true);
assert(reels[1].paused, 'Reduced motion should prevent autoplay');
""")
if failed { exit(1) }
print("PASS: JavaScript syntax, visibility playback, explicit pause, automatic resume, clip trim, and reduced motion.")
