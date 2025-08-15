// navbar
document.addEventListener("DOMContentLoaded", function () {
    const menuBtn = document.getElementById("menu-btn");
    const closeBtn = document.getElementById("close-menu");
    const mobileMenu = document.getElementById("mobile-menu");
    const links = document.querySelectorAll(".menu-link");
    const header = document.querySelector("header"); // Fixed header

    function openMenu() {
        mobileMenu.classList.remove("translate-x-full");
        document.body.classList.add("overflow-hidden");
        setTimeout(() => {
            links.forEach((link, i) => {
                setTimeout(() => link.classList.remove("opacity-0", "translate-y-4"), i * 100);
            });
        }, 150);
    }

    function closeMenu() {
        links.forEach(link => link.classList.add("opacity-0", "translate-y-4"));
        setTimeout(() => {
            mobileMenu.classList.add("translate-x-full");
            document.body.classList.remove("overflow-hidden");
        }, 250);
    }

    menuBtn.addEventListener("click", openMenu);
    closeBtn.addEventListener("click", closeMenu);

    // Smooth scroll + close menu
    links.forEach(link => {
        link.addEventListener("click", function (e) {
            const targetId = this.getAttribute("href");
            if (targetId.startsWith("#")) {
                e.preventDefault();

                const target = document.querySelector(targetId);
                if (target) {
                    const headerOffset = header.offsetHeight;
                    const elementPosition = target.getBoundingClientRect().top;
                    const offsetPosition = elementPosition + window.scrollY - headerOffset;

                    window.scrollTo({
                        top: offsetPosition,
                        behavior: "smooth"
                    });
                }
            }
            closeMenu();
        });
    });

    // Close on ESC
    document.addEventListener("keydown", (e) => {
        if (e.key === "Escape" && !mobileMenu.classList.contains("translate-x-full")) closeMenu();
    });
});

// Scroll hide/show header
document.addEventListener("DOMContentLoaded", function () {
    const header = document.getElementById("main-header");
    let lastScroll = 0;
    let ticking = false;
    let hideTimeout;

    window.addEventListener("scroll", () => {
        const currentScroll = window.pageYOffset;

        if (!ticking) {
            window.requestAnimationFrame(() => {
                if (currentScroll > lastScroll && currentScroll > header.offsetHeight) {
                    clearTimeout(hideTimeout);
                    hideTimeout = setTimeout(() => {
                        header.classList.add("-translate-y-full");
                    }, 20); // slow down hide
                } else {
                    clearTimeout(hideTimeout);
                    header.classList.remove("-translate-y-full");
                }
                lastScroll = currentScroll;
                ticking = false;
            });
            ticking = true;
        }
    });
});

//hero section carousel

var swiper = new Swiper(".progress-slide-carousel", {
loop: true,
fraction: true,
autoplay: {
  delay: 3000,
  disableOnInteraction: false,
},
pagination: {
  el: ".progress-slide-carousel .swiper-pagination",
  type: "progressbar",
},
});



// review 

var swiper = new Swiper(".mySwiper", {
        slidesPerView: 1,
        spaceBetween: 32,
        loop: true,
        centeredSlides: true,
        pagination: {
            el: ".swiper-pagination",
            clickable: true,

        },
        autoplay: {
            delay: 2500,
            disableOnInteraction: false,
        },
        breakpoints: {
        640: {
          slidesPerView: 1,
          spaceBetween: 32,
        },
        768: {
          slidesPerView: 2,
          spaceBetween: 32,
        },
        1024: {
          slidesPerView: 3,
          spaceBetween: 32,
        },
      },
    });
