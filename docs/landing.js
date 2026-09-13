(() => {
  const range = document.querySelector('#compare-range');
  range.addEventListener('input', () => document.querySelector('.compare').style.setProperty('--split', `${range.value}%`));
  const player = document.querySelector('#demo-video');
  const base = new URL('media/1.2/', new URL(document.currentScript.src));
  document.querySelector('#demo-language').addEventListener('change', (event) => {
    const locale = event.target.value;
    player.pause();
    player.poster = new URL(`${locale}-poster.jpg`, base).href;
    player.src = new URL(`${locale}-demo.mp4`, base).href;
    player.load();
  });
})();
