document.addEventListener("DOMContentLoaded", () => {
  const tabs = document.querySelectorAll(".tab-btn");
  const shapeTypeInput = document.getElementById("shape-type");
  const form = document.getElementById("calc-form");
  const loading = document.getElementById("loading");
  const resultsPanel = document.getElementById("results");
  const errorMessage = document.getElementById("error-message");
  const errorText = document.getElementById("error-text");

  // Result elements
  const resKeliling = document.getElementById("res-keliling");
  const resLuas = document.getElementById("res-luas");
  const resVolume = document.getElementById("res-volume");

  // Tab switching logic
  tabs.forEach((tab) => {
    tab.addEventListener("click", (e) => {
      // Remove active class from all
      tabs.forEach((t) => t.classList.remove("active"));
      // Add to clicked
      e.currentTarget.classList.add("active");

      // Update hidden input
      const shape = e.currentTarget.getAttribute("data-shape");
      shapeTypeInput.value = shape;

      // Optional: reset results when switching tabs
      resultsPanel.classList.add("hidden");
      errorMessage.classList.add("hidden");
    });
  });

  // Form submission
  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const shape = shapeTypeInput.value;
    const radius = document.getElementById("radius").value;
    const height = document.getElementById("height").value;

    // UI Reset
    resultsPanel.classList.add("hidden");
    errorMessage.classList.add("hidden");
    loading.classList.remove("hidden");

    try {
            // Konversi koma ke titik (Parse Float)
            const r = parseFloat(radius.replace(',', '.'));
            const t = parseFloat(height.replace(',', '.'));

            if (isNaN(r) || isNaN(t)) {
                throw new Error('Harap masukkan angka yang valid.');
            }
            if (r < 0 || t < 0) {
                throw new Error('Jari-jari dan tinggi tidak boleh negatif.');
            }

            let keliling = 0, luas = 0, volume = 0;

            if (shape === 'silinder') {
                keliling = 2 * Math.PI * r;
                luas = 2 * Math.PI * r * (r + t);
                volume = Math.PI * Math.pow(r, 2) * t;
            } else if (shape === 'kerucut') {
                keliling = 2 * Math.PI * r;
                const garis_pelukis = Math.sqrt(Math.pow(r, 2) + Math.pow(t, 2));
                luas = Math.PI * r * (r + garis_pelukis);
                volume = (1 / 3) * Math.PI * Math.pow(r, 2) * t;
            } else {
                throw new Error('Bentuk tidak valid.');
            }

            // Simulasi loading animasi dari server (Memberi jeda 600ms)
            setTimeout(() => {
                // Animate numbers
                animateValue(resKeliling, keliling);
                animateValue(resLuas, luas);
                animateValue(resVolume, volume);
                
                loading.classList.add('hidden');
                resultsPanel.classList.remove('hidden');
            }, 600);
    } catch (error) {
      loading.classList.add("hidden");
      errorText.textContent = error.message;
      errorMessage.classList.remove("hidden");
    }
  });

  // Store active animations
  const activeAnimations = new Map();

  // Simple number animation function
  function animateValue(obj, end, duration = 1000) {
    // Cancel existing animation for this element
    if (activeAnimations.has(obj)) {
      window.cancelAnimationFrame(activeAnimations.get(obj));
    }

    let startTimestamp = null;
    const step = (timestamp) => {
      if (!startTimestamp) startTimestamp = timestamp;
      const progress = Math.min((timestamp - startTimestamp) / duration, 1);
      // Easing function: easeOutQuart
      const easeOut = 1 - Math.pow(1 - progress, 4);
      const current = (easeOut * end).toFixed(2);
      obj.innerHTML = current;
      if (progress < 1) {
        const frameId = window.requestAnimationFrame(step);
        activeAnimations.set(obj, frameId);
      } else {
        obj.innerHTML = parseFloat(end).toLocaleString('id-ID', {minimumFractionDigits: 2, maximumFractionDigits: 2});
        activeAnimations.delete(obj);
      }
    };
    const frameId = window.requestAnimationFrame(step);
    activeAnimations.set(obj, frameId);
  }
});
