document.addEventListener('DOMContentLoaded', () => {
    
    // 1. Scroll Reveal Animation
    const reveals = document.querySelectorAll('.reveal');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if(entry.isIntersecting) {
                entry.target.classList.add('active');
            }
        });
    }, { threshold: 0.1 });
    reveals.forEach(el => observer.observe(el));

    // 2. Scroll Progress Bar
    window.addEventListener('scroll', () => {
        const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
        const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        document.getElementById('progressBar').style.width = (winScroll / height) * 100 + "%";
    });

    // 3. Live Love Counter
    const startDate = new Date(anniversaryDate).getTime();
    setInterval(() => {
        const now = new Date().getTime();
        const distance = now - startDate;
        
        document.getElementById("days").innerText = Math.floor(distance / (1000 * 60 * 60 * 24));
        document.getElementById("hours").innerText = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        document.getElementById("minutes").innerText = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        document.getElementById("seconds").innerText = Math.floor((distance % (1000 * 60)) / 1000);
    }, 1000);

    // 4. Interactive Letter
    document.getElementById('envelopeBtn').addEventListener('click', function() {
        this.classList.add('hidden');
        const letter = document.getElementById('letterContent');
        letter.classList.remove('hidden');
        confetti({ particleCount: 50, spread: 60, origin: { y: 0.8 } });
    });

    // 5. Happiness Button
    document.getElementById('smileBtn').addEventListener('click', () => {
        const randomIndex = Math.floor(Math.random() * smileReasons.length);
        const reasonEl = document.getElementById('smileReason');
        reasonEl.innerText = `"${smileReasons[randomIndex]}"`;
        reasonEl.classList.remove('hidden');
        confetti({ particleCount: 100, spread: 100 });
    });

    // 6. Music Player
    const musicBtn = document.getElementById('musicBtn');
    const bgMusic = document.getElementById('bgMusic');
    let isPlaying = false;
    musicBtn.addEventListener('click', () => {
        if(isPlaying) {
            bgMusic.pause();
            musicBtn.innerText = '🎵';
        } else {
            bgMusic.play();
            musicBtn.innerText = '⏸️';
        }
        isPlaying = !isPlaying;
    });

    // 7. Easter Egg Secret Heart
    document.getElementById('secretHeart').addEventListener('click', () => {
        alert("You found a secret! I love you to the moon and back! 🌙✨");
        confetti({ particleCount: 200, spread: 160 });
    });

    // 8. Final Scene Confetti
    const finalObserver = new IntersectionObserver((entries) => {
        if(entries[0].isIntersecting) {
            confetti({ particleCount: 150, spread: 100, origin: { y: 0.6 } });
            finalObserver.disconnect();
        }
    }, { threshold: 0.5 });
    finalObserver.observe(document.getElementById('finalScene'));

    // --- 9. ANTI-CLUMPING BACKGROUND STICKERS ---
    const bgContainer = document.getElementById('floating-stickers');
    const stickerImages = ['bg_1.png', 'bg_2.png', 'bg_3.png', 'bg_4.png', 'bg_5.png'];
    const totalStickers = 6; // Reduced to 6 for a cleaner look

    // We divide the screen into a grid (3 columns x 2 rows)
    const cols = 3;
    const rows = 2;
    let index = 0;

    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (index >= totalStickers) break;

            const img = document.createElement('img');
            const randomImg = stickerImages[Math.floor(Math.random() * stickerImages.length)];
            img.src = `/static/images/${randomImg}`;
            
            // Set opacity to 20% so they are subtle
            img.className = 'absolute opacity-20 animate-sticker object-contain'; 
            
            // Calculate grid boundaries
            const cellWidth = 100 / cols;
            const cellHeight = 100 / rows;
            
            // Place sticker randomly inside its dedicated cell (prevents clumping)
            const randomX = (c * cellWidth) + 5 + Math.random() * (cellWidth - 15);
            const randomY = (r * cellHeight) + 5 + Math.random() * (cellHeight - 15);
            
            img.style.left = `${randomX}vw`;
            img.style.top = `${randomY}vh`;
            
            // Slightly smaller sizes (80px to 160px)
            const size = Math.random() * 80 + 80; 
            img.style.width = `${size}px`;
            img.style.height = `${size}px`;
            
            img.style.animationDelay = `${Math.random() * 5}s`;
            img.style.animationDuration = `${Math.random() * 10 + 15}s`;
            
            bgContainer.appendChild(img);
            index++;
        }
    }
});