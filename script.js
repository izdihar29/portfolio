document.addEventListener('DOMContentLoaded', () => {
  const navbar = document.getElementById('navbar');
  const hamburger = document.getElementById('hamburger');
  const navLinks = document.querySelector('.nav-links');
  const contactForm = document.getElementById('contactForm');
  const formMessage = document.getElementById('formMessage');
  const statNumbers = document.querySelectorAll('.stat-number');
  const fadeEls = document.querySelectorAll('.fade-in');

  navbar.classList.add('scrolled');

  window.addEventListener('scroll', () => {
    navbar.classList.toggle('scrolled', window.scrollY > 50);
  });

  hamburger.addEventListener('click', () => {
    navLinks.classList.toggle('active');
  });

  navLinks.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      navLinks.classList.remove('active');
    });
  });

  const observerOptions = {
    threshold: 0.2,
    rootMargin: '0px 0px -50px 0px'
  };

  const fadeObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
      }
    });
  }, observerOptions);

  fadeEls.forEach(el => fadeObserver.observe(el));

  const projectsEl = document.getElementById('projects');
  const statsObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        let current = 0;
        const increment = 3 / 60;
        const timer = setInterval(() => {
          current += increment;
          if (current >= 3) {
            projectsEl.textContent = '3+';
            clearInterval(timer);
          } else {
            projectsEl.textContent = Math.floor(current) + '+';
          }
        }, 30);
        statsObserver.disconnect();
      }
    });
  }, { threshold: 0.5 });

  const statsSection = document.querySelector('.about-stats');
  if (statsSection) statsObserver.observe(statsSection);

contactForm.addEventListener('submit', async (e) => {
  e.preventDefault();
  const name = document.getElementById('name').value.trim();
  const email = document.getElementById('email').value.trim();
  const message = document.getElementById('message').value.trim();

  if (!name || !email || !message) {
    formMessage.textContent = 'Please fill in all fields.';
    formMessage.className = 'form-message error';
    return;
  }

  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email)) {
    formMessage.textContent = 'Please enter a valid email address.';
    formMessage.className = 'form-message error';
    return;
  }

  formMessage.textContent = 'Sending...';
  formMessage.className = 'form-message';

  try {
    const response = await fetch(contactForm.action, {
      method: 'POST',
      body: new FormData(contactForm),
      headers: { 'Accept': 'application/json' }
    });
    if (response.ok) {
      formMessage.textContent = 'Message sent successfully! 🎉';
      formMessage.className = 'form-message success';
      contactForm.reset();
      setTimeout(() => { formMessage.textContent = ''; }, 5000);
    } else {
      const err = await response.json();
      formMessage.textContent = err.errors?.map(e => e.message).join(', ') || 'Something went wrong.';
      formMessage.className = 'form-message error';
    }
  } catch (err) {
    formMessage.textContent = 'Something went wrong. Please try again.';
    formMessage.className = 'form-message error';
  }
});
});