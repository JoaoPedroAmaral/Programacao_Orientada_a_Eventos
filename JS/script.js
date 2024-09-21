document.addEventListener('DOMContentLoaded', function() {
    const text = "pressione START para começar!";
    const typingText = document.getElementById('typing-text');
    let i = 0;

    function typeWriter() {
        if (i < text.length) {
            typingText.textContent += text.charAt(i);
            i++;
            setTimeout(typeWriter, 100);  // Velocidade de digitação (em ms)
        }
    }

    typeWriter();  // Inicia a animação de digitação
});

/*BTN sound*/ 

document.getElementById('clickButton').addEventListener('click', function() {
    const apresentacao = document.getElementById("apresentacao")
    const TitlePy = document.getElementById("TitlePy")
    const dinossauroBK = document.getElementById("BK")
    const OrientadoAEvento1 = document.getElementById("OrientadoAEvento1")
    const OrientadoAEvento2 = document.getElementById("OrientadoAEvento2")
    if(apresentacao.classList == "apresentacaoDark"){
        apresentacao.classList.toggle("apresentacaoDark");
        apresentacao.classList.toggle("apresentacao")
        TitlePy.classList.toggle("titleOEDark");
        TitlePy.classList.toggle("titleOE");
        dinossauroBK.classList.toggle("dinossauroBKDark");
        dinossauroBK.classList.toggle("dinossauroBK");
        OrientadoAEvento1.style.opacity = '1';
        OrientadoAEvento2.style.opacity = '0';
        document.getElementById("btnNextDark").style.display = 'none'
        document.querySelector('.linkNext').style.display = 'flex'
    }
    document.getElementById('clickAudio').play();
});

/*Mudar BackGround*/ 
document.querySelector('.linkNext').addEventListener('click', function(e) {
    e.preventDefault();  // Prevents the default link behavior
    const apresentacao = document.getElementById("apresentacao")
    const TitlePy = document.getElementById("TitlePy")
    const dinossauroBK = document.getElementById("BK")
    const OrientadoAEvento1 = document.getElementById("OrientadoAEvento1")
    const OrientadoAEvento2 = document.getElementById("OrientadoAEvento2")
    if(apresentacao.classList == "apresentacao"){
        apresentacao.classList.toggle("apresentacaoDark");
        apresentacao.classList.toggle("apresentacao")
        TitlePy.classList.toggle("titleOEDark");
        TitlePy.classList.toggle("titleOE");
        dinossauroBK.classList.toggle("dinossauroBKDark");
        dinossauroBK.classList.toggle("dinossauroBK");
        OrientadoAEvento1.style.opacity = '0';
        OrientadoAEvento2.style.opacity = '1';
        document.getElementById("btnNextDark").style.display = 'flex'
        document.querySelector('.linkNext').style.display = 'none'
    }
    document.getElementById('clickAudio').play();
});


document.querySelector('.linkNextDark').addEventListener('click', function(e) {

    document.getElementById('clickAudio').play();
});