const search_box = document.querySelector('#SearchBox')
const search_box_button = document.querySelector('#SearchBoxButton')

const togglers = document.getElementsByClassName('toggler')

for (let toggler of togglers) {
    toggler.addEventListener('click', (ev) => {
        let selector = ev.target.getAttribute('data-selector')
        let elements = document.querySelectorAll(selector)

        for (let el of elements) {
            let display_param = el.style.display
            el.style.display = (display_param == 'none' || display_param == '') ? 'flex' : 'none'
        }
    })
}