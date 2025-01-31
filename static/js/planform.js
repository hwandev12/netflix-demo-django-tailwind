document.addEventListener("DOMContentLoaded", () => {

    const priceItem = document.querySelectorAll(".price_item")
    const btn = document.querySelector(".btn")

    let selectedPlan = ""
    
    priceItem.forEach((item) => {
        item.addEventListener("click", (event) => {
            priceItem.forEach((i) => {
                if (i !== item) {
                    i.querySelector(".fa-check").classList.remove("active__icon")
                    i.classList.remove("active__shadow")
                }
            })
            item.querySelector(".fa-check").classList.toggle("active__icon")
            item.classList.toggle("active__shadow")
            selectedPlan = item.getAttribute("data-plan")
            btn.addEventListener("click", () => {
                if(selectedPlan.length > 0)
                localStorage.setItem("PLAN", selectedPlan)
                window.location.href = '/auth/signup/registration/'
            })
        })
    })

})

