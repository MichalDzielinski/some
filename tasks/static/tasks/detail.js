// BUTTONS
const runBtn = document.getElementById('run-btn')
const endBtn = document.getElementById('end-btn')
const breakBtn = document.getElementById('break-btn')

const timer = document.getElementById('timer')
const lightBulb = document.getElementById('light-bulb')

const alertBox = document.getElementById('alert-box')

let time = timer.textContent
let manageInterval

const getCookie = (name) => {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
};


  
const csrftoken = getCookie("csrftoken");

const sendData = (data) => {
    data['csrfmiddlewaretoken']  = csrftoken

    $.ajax({
        type: 'POST',
        url: './log/',
        data,
        success: (resp) => {
            console.log(resp);
            const {message} = resp
            alertBox.classList.remove('d-none')
            alertBox.innerHTML = message
        },
        error: (err) => {
            console.log(err)
        }

    })
}

endBtn.addEventListener('click', () => {
    runBtn.classList.remove('d-none')
    breakBtn.classList.remove('d-none')
    endBtn.classList.add('d-none')
    
    if (lightBulb.classList.contains('d-none')){
        lightBulb.classList.remove('d-none')
    }
    
    clearInterval(manageInterval)
    time  = "00:00:00"
    timer.textContent = time

    data = {
        is_finish: true,
    }

    sendData(data)
})

runBtn.addEventListener('click', () => {
    runBtn.classList.add('d-none')
    breakBtn.classList.add('d-none')
    endBtn.classList.remove('d-none')

    activateTimer()

    data = {
        is_work: true,
        is_finish: false,
    }

    sendData(data)

} )

breakBtn.addEventListener('click', () => {
    runBtn.classList.add('d-none')
    breakBtn.classList.add('d-none')
    endBtn.classList.remove('d-none')

    activateTimer()

    data = {
        is_work: false,
        is_finish: false,
    }

    sendData(data)
    

} )

window.addEventListener('beforeunload', () => {
    if(time !== '00:00:00'){
        const data = {
            is_finish: true
        }
        sendData(data)
    }
})


const activateTimer = () => {
    let displayHours, displayMinutes, displaySeconds
    let[hours, minutes, seconds] = time.split(":").map(Number)
    

    manageInterval = setInterval(() => {
        seconds++
        if( seconds === 60){
            seconds = 0
            minutes++
        }

        if (minutes === 60){
            minutes = 0
            hours++
        }
        displayHours = hours.toString().padStart(2, '0')
        displayMinutes = minutes.toString().padStart(2, '0')
        displaySeconds = seconds.toString().padStart(2, '0')

        if(seconds % 2 === 0){
            lightBulb.classList.remove("d-none")


        }
        else
        {
            lightBulb.classList.add("d-none")

        }

        time = `${displayHours}:${displayMinutes}:${displaySeconds}`
        timer.textContent = time
    }, 1000)
}