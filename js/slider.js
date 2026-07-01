window.addEventListener("load", () => {
    const track = document.querySelector(".track");

    // Duplicate images
    track.innerHTML += track.innerHTML;

    let position = 0;

    const gap = parseInt(getComputedStyle(track).gap) || 0;
    const imageWidth = track.querySelector("img").getBoundingClientRect().width + gap;
    const totalWidth = imageWidth * (track.children.length / 2);

    function animate() {
        position += 0.5;

        if (position >= totalWidth) {
            position = 0;
        }

        track.style.transform = `translateX(-${position}px)`;

        requestAnimationFrame(animate);
    }

    animate();
});