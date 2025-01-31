document.addEventListener("DOMContentLoaded", () => {
  const banner = document.querySelector(".modal__image");
  const video = document.querySelector(".modal__video video");
  const mainPLIC = document.querySelector(".modal__image i");
  const modal = document.querySelector(".modal__video");
  const exitModalICON = document.querySelector(".exit__modal");
  const playICON = document.querySelector(".controls .play__custom");
  const expandICON = document.querySelector(".controls .fa-expand");

  const watchNow = document.querySelector(".watch__now");
  const controls = document.querySelector(".controls");
  const progress = document.querySelector(".progress");
  const progressWrapper = document.querySelector(".progress__wrapper");
  const videoWrapper = document.querySelector(".video__wrapper");

  const volumeInput = document.querySelector(".volume__input");
  const volumeIcon = document.querySelector(".volume__icon");

  const videoDuration = document.querySelector(".movie__time");

  const trailerLoader = document.querySelector(".loader__trailer");
  const movieSingle = document.querySelectorAll(".movie__single");

  const blueBackground = document.querySelector(".blur__background")

  blueBackground.style.height = document.body.clientHeight + "px";

  setTimeout(() => {
    trailerLoader.classList.add("hidden");
    trailerLoader.classList.remove("flex");
    movieSingle.forEach((m) => {
      m.classList.remove("hidden");
      m.classList.add("flex");
    });
  }, 3000);

  let volume = 0;
  let isPlaying = false;
  let isFullScreen = false;

  volumeIcon.addEventListener("click", () => {
    if (video.volume == 0) {
      volumeIcon.classList.remove("fa-volume-xmark");
      volumeIcon.classList.add("fa-volume-high");
      volumeInput.value = volume;
      video.volume = volume / 100;
    } else {
      video.volume = 0;
      volumeIcon.classList.remove("fa-volume-high");
      volumeIcon.classList.add("fa-volume-xmark");
      volume = volumeInput.value;
      volumeInput.value = 0;
    }
  });

  volumeInput.addEventListener("input", () => {
    video.volume = volumeInput.value / 100;
    if (video.volume == 0) {
      volumeIcon.classList.remove("fa-volume-high");
      volumeIcon.classList.add("fa-volume-xmark");
    } else {
      volumeIcon.classList.add("fa-volume-high");
      volumeIcon.classList.remove("fa-volume-xmark");
    }
  });

  const updateProgress = () => {
    const currentTime = video.currentTime;
    const duration = video.duration;
    const progressPercent = (currentTime / duration) * 100;
    progress.style.width = `${progressPercent}%`;
    requestAnimationFrame(updateProgress);
    const formatTime = (time) => {
      const minutes = Math.floor(time / 60);
      const seconds = Math.floor(time % 60)
        .toString()
        .padStart(2, "0");
      return `${minutes}:${seconds}`;
    };
    videoDuration.innerHTML = `
    <span class='flex items-center gap-2'><span>${formatTime(
      currentTime
    )}</span> / <span>${formatTime(duration)}</span></span>
    `;
  };

  video.addEventListener("play", () => {
    requestAnimationFrame(updateProgress);
    video.volume = volumeInput.value / 100;
  });

  progressWrapper.addEventListener("click", (event) => {
    const clickPosition = event.offsetX;
    const duration = video.duration;
    const progressWidth = progressWrapper.offsetWidth;

    // Calculate the new time based on click position and progress bar width
    const newTime = (clickPosition / progressWidth) * duration;
    // Update the video current time
    video.currentTime = newTime;
  });

  mainPLIC.addEventListener("click", () => {
    isPlaying = true;
    video.classList.toggle("hidden");
    banner.classList.remove("flex");
    banner.classList.add("hidden");
    video.play();
    controls.classList.remove("hidden");
    controls.classList.add("flex");
    playICON.classList.remove("fa-play");
    playICON.classList.add("fa-pause");
  });

  exitModalICON.addEventListener("click", () => {
    isPlaying = false;
    modal.classList.add("hidden");
    modal.classList.remove("flex");
    video.classList.add("hidden");
    banner.classList.add("flex");
    banner.classList.remove("hidden");
    document.body.style.overflow = "auto";
    controls.classList.add("hidden");
    controls.classList.remove("flex");
    video.pause();
  });

  watchNow.addEventListener("click", () => {
    modal.classList.remove("hidden");
    modal.classList.add("flex");
    document.body.style.overflow = "hidden";
  });

  document.addEventListener("keydown", (event) => {
    if (isPlaying) {
      if (event.key === " ") {
        if (video.paused) {
          video.play();
          playICON.classList.remove("fa-play");
          playICON.classList.add("fa-pause");
        } else {
          video.pause();
          playICON.classList.add("fa-play");
          playICON.classList.remove("fa-pause");
        }
      }
    }
  });

  video.addEventListener("click", () => {
    if (video.paused) {
      video.play();
      playICON.classList.remove("fa-play");
      playICON.classList.add("fa-pause");
    } else {
      video.pause();
      playICON.classList.add("fa-play");
      playICON.classList.remove("fa-pause");
    }
  });

  playICON.addEventListener("click", () => {
    if (video.paused) {
      video.play();
      playICON.classList.remove("fa-play");
      playICON.classList.add("fa-pause");
    } else {
      video.pause();
      playICON.classList.add("fa-play");
      playICON.classList.remove("fa-pause");
    }
  });

  document.body.addEventListener("keydown", (e) => {
    if (e.key == "f") {
      document.body.style.overflow = "hidden";
      if (!document.fullscreenElement) {
        if (document.documentElement.requestFullscreen) {
          isFullScreen = true;
          document.documentElement.requestFullscreen();
        } else if (document.documentElement.webkitRequestFullscreen) {
          // For older versions of Safari
          isFullScreen = true;
          document.documentElement.webkitRequestFullscreen();
        }
        // Set screen orientation to landscape
        screen.orientation.lock("landscape");
      } else {
        document.exitFullscreen(); // Exit fullscreen mode
        // Unlock screen orientation
        screen.orientation.unlock();
        isFullScreen = false;
      }
    }
  });

  document.addEventListener("fullscreenchange", toggleCustomControls);

  expandICON.addEventListener("click", () => {
    isFullScreen = true;
    document.body.style.overflow = "hidden";
    if (!document.fullscreenElement) {
      if (document.documentElement.requestFullscreen) {
        document.documentElement.requestFullscreen();
      } else if (document.documentElement.webkitRequestFullscreen) {
        // For older versions of Safari
        document.documentElement.webkitRequestFullscreen();
      }
      // Set screen orientation to landscape
      screen.orientation.lock("landscape");
    } else {
      document.exitFullscreen(); // Exit fullscreen mode
      // Unlock screen orientation
      screen.orientation.unlock();
    }
  });

  videoWrapper.addEventListener("dblclick", () => {
    isFullScreen = true;
    document.body.style.overflow = "hidden";
    if (!document.fullscreenElement) {
      if (document.documentElement.requestFullscreen) {
        document.documentElement.requestFullscreen();
      } else if (document.documentElement.webkitRequestFullscreen) {
        // For older versions of Safari
        document.documentElement.webkitRequestFullscreen();
      }
      // Set screen orientation to landscape
      screen.orientation.lock("landscape");
    } else {
      document.exitFullscreen(); // Exit fullscreen mode
      // Unlock screen orientation
      screen.orientation.unlock();
    }
  });

  function toggleCustomControls() {
    document.body.style.overflow = "hidden";
    if (document.fullscreenElement) {
      isFullScreen = true;
      document.body.style.overflow = "hidden";
      videoWrapper.style.width = "100%";
      videoWrapper.style.height = "100dvh";
      screen.orientation.lock("landscape");
      setTimeout(() => {
        if (isFullScreen) {
          controls.classList.remove("flex");
          controls.classList.add("hidden");
        }
      }, 5000);
    } else {
      isFullScreen = false;
      videoWrapper.style.width = "70rem";
      videoWrapper.style.height = "40rem";
      controls.classList.add("flex");
      controls.classList.remove("hidden");
      screen.orientation.unlock();
    }
  }

  videoWrapper.addEventListener("mousemove", () => {
    if (document.fullscreenElement) {
      document.addEventListener("keydown", (e) => {
        if (e.key == " " && isPlaying) {
          controls.classList.add("flex");
          controls.classList.remove("hidden");
          setTimeout(() => {
            if (isFullScreen) {
              console.log(isFullScreen);
              controls.classList.remove("flex");
              controls.classList.add("hidden");
            }
          }, 5000);
        }
      });
      controls.classList.add("flex");
      controls.classList.remove("hidden");
      setTimeout(() => {
        if (isFullScreen) {
          console.log(isFullScreen);

          controls.classList.remove("flex");
          controls.classList.add("hidden");
        }
      }, 5000);
    }
  });


});
