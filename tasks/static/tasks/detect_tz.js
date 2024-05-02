const timezone = Intl.DateTimeFormat().resolvedOptions().timeZone
console.log(timezone)

 // ajax request in main page -> different view -> 
 // update timezone -> get response in the main page

 const url = `/detect-tz/?timezone=${timezone}`

 $.ajax({
    type: "GET",
    url,
    success: (resp) => {
        const {msg, is_changed} = resp
        console.log('response: ', msg)
        if (is_changed) {
            alert(msg + " - you can change it manually by clicking on the username")
        }

    },
    error: (err) => console.log('error: ', err)
 })
