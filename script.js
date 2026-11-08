// Keep the published clip trim and play muted reels only while visible.
// Native controls also work when JavaScript or autoplay is unavailable.
const videos = [...document.querySelectorAll('video')];
const motionPreference = window.matchMedia('(prefers-reduced-motion: reduce)');
const states = new WeakMap();

for (const video of videos) {
  const state = { visible: false, userPaused: false };
  states.set(video, state);
  video.addEventListener('pause', () => {
    if (state.visible && !video.ended) state.userPaused = true;
  });
  video.addEventListener('play', () => { state.userPaused = false; });

  const end = Number(video.dataset.end);
  if (end > 0) {
    video.addEventListener('timeupdate', () => {
      if (video.currentTime >= end && !video.paused) video.currentTime = 0;
    });
    video.addEventListener('seeking', () => {
      if (video.currentTime > end) video.currentTime = 0;
    });
    // Media fragments can stop at the trim before timeupdate fires.
    video.addEventListener('ended', () => {
      if (state.visible && !state.userPaused && !motionPreference.matches) {
        video.currentTime = 0;
        video.play().catch(() => {});
      }
    });
  }
}

if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver(entries => {
    for (const entry of entries) {
      const video = entry.target;
      const state = states.get(video);
      state.visible = entry.isIntersecting;
      if (state.visible && !state.userPaused && !motionPreference.matches) {
        video.play().catch(() => {});
      } else if (!state.visible && !video.paused) {
        video.pause();
      }
    }
  }, { threshold: 0.3 });
  videos.forEach(video => observer.observe(video));
}

motionPreference.addEventListener('change', event => {
  if (event.matches) videos.forEach(video => video.pause());
});
