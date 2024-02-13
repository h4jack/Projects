const websiteList = document.querySelector('.website-list');
const websiteItems = websiteList.querySelectorAll('.website-item');

websiteItems.forEach((item, index) => {
  const websitePreview = item.querySelector('.website-preview');
  const websiteDetails = item.querySelector('.website-details');
  const websiteCta = item.querySelector('.go-button');
  const websiteUrl = `https://codepen.io/shshaw/full/ExeXdRd`; // replace with actual URL

  websiteCta.addEventListener('click', () => {
    const iframe = document.createElement('iframe');
    iframe.src = websiteUrl;
    iframe.width = '100%';
    iframe.height = '100%';
    iframe.frameBorder = '0';
    iframe.allow = 'fullscreen';
    iframe.allowFullscreen = true;

    websitePreview.innerHTML = '';
    websitePreview.appendChild(iframe);
    websiteDetails.style.display = 'none';
  });

  const closeButton = item.querySelector('.close-button');
  closeButton.addEventListener('click', () => {
    const iframe = closeButton.parentElement;
    const src = iframe.getAttribute('data-src');

    iframe.src = '';
    iframe.style.display = 'none';
    websiteDetails.style.display = 'flex';
  });

  if (index === 0) {
    item.classList.add('active');
    websitePreview.appendChild(websiteDetails);
  }
});

const websiteTitles = websiteList.querySelectorAll('.website-title');

websiteTitles.forEach((title, index) => {
  title.addEventListener('click', () => {
    const activeItem = websiteList.querySelector('.active');
    const targetItem = websiteList.querySelector(`#cl${index + 1}`);

    if (activeItem && activeItem !== targetItem) {
      activeItem.classList.remove('active');
      activeItem.querySelector('.website-details').style.display = 'flex';
      activeItem.querySelector('.website-preview').innerHTML = '';
    }

    targetItem.classList.toggle('active');
    if (targetItem.classList.contains('active')) {
      const websitePreview = targetItem.querySelector('.website-preview');
      const iframe = websitePreview.querySelector('iframe');
      const src = iframe.getAttribute('data-src');

      iframe.src = src;
      iframe.style.display = 'block';
    }
  });
});