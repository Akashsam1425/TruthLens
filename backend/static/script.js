// ================================
// TruthLens v1.0
// Dashboard Animations
// ================================

document.addEventListener("DOMContentLoaded", () => {

    // Animate Progress Bar
    const progressBar = document.querySelector(".progress-bar");

    if(progressBar){

        const width = progressBar.style.width;

        progressBar.style.width = "0%";

        setTimeout(() => {

            progressBar.style.width = width;

        },300);

    }

    // Animate Statistic Cards
    const cards = document.querySelectorAll(".stat-card");

    cards.forEach((card,index)=>{

        card.style.opacity="0";

        card.style.transform="translateY(25px)";

        setTimeout(()=>{

            card.style.transition=".5s";

            card.style.opacity="1";

            card.style.transform="translateY(0px)";

        },index*120);

    });

});