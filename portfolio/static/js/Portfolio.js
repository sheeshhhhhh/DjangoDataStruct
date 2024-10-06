

function sendMessage() {
    message = document.getElementById("message")
    Name = document.getElementById("name").value
    contact = document.getElementById("Contact").value

    // validating the message
    if(!message.value) {
        // displaying error message
        messageError = document.getElementById("messageError")
        messageError.innerHTML = "Message is Required"

        styleTextAreaError()
        return 
    } 

    // fetching the data
    fetchMessage(message.value, Name, contact)
}

// this is use to make text area look error
function styleTextAreaError() {
    message = document.getElementById("message")
    message.style.border = "2px solid red"
}

function styleTextAreaErrorRemove() {
    message = document.getElementById("message")
    message.style.border = ""
    messageError = document.getElementById("messageError")
     messageError.innerHTML = ""
}

function showToast(text, type="success") {
    if(!text) {
        throw new Error("Text is Required")
    }

    let bgColor = "#588157" 

    if(type === "destructive") {
        bgColor = "red"
    }

    Toastify({
        text: text,
        duration: 3000,
        style: {
            background: bgColor,
            color: "#fff",
            fontWeight: "bold",
            borderRadius: "12px"
        },
        position: "center",
    }).showToast();

}

async function fetchMessage(message, name, contact) {
    try {
        const response = await fetch("/api/sendMessage/", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                message: message,
                name: name || "",
                contact: contact || ""
            })
        })

        const data = await response.json()

        if(data.status === "fail") {
            throw new Error(data.error)
        }

        //successfully sent message!
        styleTextAreaErrorRemove()
        // reseting value
        document.getElementById("Contact").value = ""
        document.getElementById("message").value = ""
        document.getElementById("name").value = ""

        showToast("Successfully Sent a Message")
    } catch (error) {
        console.log(error)
        showToast(error.message, "destructive")
    }
        
}