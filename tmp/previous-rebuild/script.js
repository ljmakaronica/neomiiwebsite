// Play the original local reels only while they are in view. Native controls
// remain available, and a visitor's explicit pause is respected.
const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
if ('IntersectionObserver' in window && !reduceMotion) {
  const states = new WeakMap();
  const observer = new IntersectionObserver(entries => {
    for (const entry of entries) {
      const video = entry.target;
      const state = states.get(video);
      state.visible = entry.isIntersecting;
      if (entry.isIntersecting && !state.userPaused) {
        video.play().catch(() => {});
      } else if (!entry.isIntersecting && !video.paused) {
        video.pause();
      }
    }
  }, { threshold: 0.3 });
  for (const video of document.querySelectorAll('video')) {
    const state = { visible: false, userPaused: false };
    states.set(video, state);
    video.addEventListener('pause', () => { if (state.visible) state.userPaused = true; });
    video.addEventListener('play', () => { state.userPaused = false; });
    observer.observe(video);
  }
}
