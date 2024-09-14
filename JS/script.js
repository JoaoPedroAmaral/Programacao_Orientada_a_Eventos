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

document.getElementById('clickButton').addEventListener('click', function() {
    document.getElementById('clickAudio').play();
});