window.addEventListener("load", onLoad)

function onLoad() {
    const btnConnectToUs = document.getElementsByClassName('hiddenContactFormBtn')[0]
    const formWrapper = document.getElementsByClassName('form-wrapper')[0]
    const connect = document.getElementsByClassName('contactFormWrapper')[0]
    connect.id = 'hide'
    const foot = document.getElementsByClassName('footer')[0]

    const emptyDiv = document.createElement('div')
    connect.replaceChildren(emptyDiv)


    btnConnectToUs.addEventListener('click', connectToUs)


    function connectToUs() {
        connect.replaceChildren(formWrapper)
        if (connect.id === 'hide') {
            connect.style.display = 'grid'
            connect.id = 'show'
            // foot.style.backgroundColor = '#e68b5e'

        } else {
            connect.style.display = 'none'
            connect.id = 'hide'
            // foot.style.backgroundColor = '#ffffff'

        }


    }
}

