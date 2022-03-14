const toggleButton = document.getElementsByClassName('toggle_button')[0]
const navbarLinks = document.getElementsByClassName('navigation_list')[0]

toggleButton.addEventListener('click', () => {
    navbarLinks.classList.toggle('active')
})