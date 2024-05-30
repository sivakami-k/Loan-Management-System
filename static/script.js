/**
 * Created by sivak on 21-11-2023.
 */
// You may not need this script if you are using inline JavaScript

// Optionally, if you have multiple images, you can use the following code to apply zoom to all images with the 'zoom-image' class:
// document.querySelectorAll('.zoom-image').forEach(image => {
//     image.addEventListener('mouseenter', handleMouseEnter);
//     image.addEventListener('mouseleave', handleMouseLeave);
// });

// Otherwise, if you only have one image, you can use the following:

const zoomImage = document.getElementById('zoomImage');

zoomImage.addEventListener('mouseenter', handleMouseEnter);
zoomImage.addEventListener('mouseleave', handleMouseLeave);

function handleMouseEnter() {
    zoomImage.style.transform = 'scale(1.5)';
}

function handleMouseLeave() {
    zoomImage.style.transform = 'scale(1)';
}
