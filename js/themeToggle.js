document.addEventListener('DOMContentLoaded', () => {
  const toggleBtn = document.getElementById('themeToggle')
  const html = document.documentElement
  const iconLight = document.getElementById('iconLight')
  const iconDark = document.getElementById('iconDark')

  function updateIcon() {
    const isDark = html.classList.contains('dark')
    iconLight?.classList.toggle('hidden', isDark)
    iconDark?.classList.toggle('hidden', !isDark)
  }

  if (toggleBtn) {
    updateIcon()

    toggleBtn.addEventListener('click', () => {
      const isDark = html.classList.toggle('dark')
      localStorage.theme = isDark ? 'dark' : 'light'
      updateIcon()
    })
  }
})
