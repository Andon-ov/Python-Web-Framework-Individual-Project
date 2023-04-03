window.addEventListener("load", onLoad)

function onLoad() {
    const btnConnectToUs = document.getElementsByClassName('hiddenContactFormBtn')[0]
    const formWrapper = document.getElementsByClassName('form-wrapper')[0]
    const connect = document.getElementsByClassName('contactFormWrapper')[0]
    if (connect) {
        connect.id = 'hide'

        const emptyDiv = document.createElement('div')
        connect.replaceChildren(emptyDiv)
        btnConnectToUs.addEventListener('click', connectToUs)
    }


    function connectToUs() {
        connect.replaceChildren(formWrapper)
        if (connect.id === 'hide') {
            connect.style.display = 'grid'
            connect.id = 'show'

        } else {
            connect.style.display = 'none'
            connect.id = 'hide'
        }
    }

// modal

    let modal = document.getElementById("myModal");

    // Get the button that opens the modal
    let btn = document.getElementById("myBtn");
    btn.addEventListener('click', openModal)


    // Get the <span> element that closes the modal
    let span = document.getElementsByClassName("close")[0];

    // When the user clicks the button, open the modal
    function openModal() {
        modal.style.display = "block";
        console.log('test')
    }


    // When the user clicks on <span> (x), close the modal
    span.onclick = function () {
        modal.style.display = "none";
    }

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function (event) {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    }
}

