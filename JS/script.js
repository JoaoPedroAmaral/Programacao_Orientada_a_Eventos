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
let currentTextIndex;

document.getElementById('clickButton').addEventListener('click', function() {
    const apresentacao = document.getElementById("apresentacao")
    const TitlePy = document.getElementById("TitlePy")
    const dinossauroBK = document.getElementById("BK")

    currentTextIndex = 0;
    // Seleciona o elemento do texto e botão
    const textElement = document.getElementById("textPOE");
    const titleElement = document.getElementById("titlePOE");
    const nextButton = document.getElementById("btnPOE");

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
    
    titleElement.textContent = titles[currentTextIndex];
    textElement.textContent = texts[currentTextIndex];
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

function changeContentMobile() {

    var mobilepart =document.getElementById('Part1Mobile');
    mobilepart.innerHTML = 'Qual a utilidade do Python?!';
    var textmobile = document.getElementById('textArea1');
    textmobile.innerHTML = `<li>Desenvolvimento web do lado do servidor...</li>
        <li>Automação com scripts Python...</li>
        <li>Ciência de dados e Machine Learning...</li>
        <li>Automação de Testes de software...</li>`;

    var TitlePyMobile = document.getElementById('TitlePyMobile');
    TitlePyMobile.style.color = "white"
    mobilepart.style.color = "white"
    textmobile.style.color = "white"

    // Muda o background para o segundo
    document.getElementById('BKMobile').style.backgroundImage = "url(../IMG/DaycenarychomeDark.png)";
    document.getElementById('apresentacao').style.backgroundColor = "#5c5c5c";
}



 // Textos a serem exibidos
 const texts = [
    "A programação orientada a eventos em Python tem sua abordagem implementada por meio de bibliotecas e frameworks, os quais fornecem suporte para lidar com eventos, tais como Tkinter (biblioteca padrão do Python que permite a criação de interfaces gráficas), Twisted (um framework assíncrono que permite a criação de aplicativos de rede escaláveis) e Pygame (uma biblioteca bastaten conhecida para o desenvolvimento de jogo), sendo o último exemplo a biblioteca utilizada para a criação do jogo.",
    "A programação orientada a eventos é um paradigma de programação onde o fluxo de execução do programa segue um controle de fluxo guiado por indicações externas, os eventos, desempenhando um papel essencial em interfaces de usuários e sistemas reativos. Sistemas programados utilizando o paradigma orientado a eventos são codados em sua base um loop de eventos, que recebem repetidamente informações para processar e disparar uma função de resposta de acordo com o evento, ou seja, o programa não determina a ordem da sequência de operações executadas.<br> Um dos melhores exemplos para descrever a programação orientada a eventos e explicar o que é um evento na área da computação são as GUI’s (Graphical User Interface). Em uma aplicação baseada em interface gráfica de usuário, os eventos acionados pelo usuário são gerados ao interagir com a interface, como clique do mouse em um botão, escrever uma caixa de texto, selecionar uma opção de um menu e fechar/redimensionar uma janela, portanto, quando um usuário interage com um componente GUI, essa interação é conhecida como evento, que após ser acionado, o programa vai reagir a esses evento e realizar a operação desejada, essa resposta é chamada de handler ou manipulador de evento.<br>" +
    "   Além disso, a programação orientada a eventos também é utilizada para o desenvolvimento de aplicações web, onde os eventos podem ser o envio de um formulário ou o recebimento de dados em uma API. Um outro exemplo bastante comum é no desenvolvimento de jogo, onde os eventos podem ser movimentos do jogador ou colisões objetos",
    "A programação orientada a eventos possui diversas vantagens, dentre elas está a modularidade, capacidade de suportar processamento assíncrono, flexibilidade e adequação para as interfaces gráficas.<br> <span class='textSpanPOE1'> Modularidade: </span>  A modularidade se baseia na capacidade de dividir o programa em módulos independentes, podendo ser testados separadamente e, consequentemente, facilitando a manutenção e o reuso de código, tornando o desenvolvimento mais eficiente.<br> <span class='textSpanPOE1'> Processamento Assíncrono:</span> Eventos assíncronos são eventos que ocorrem em momentos diferentes e não necessariamente em uma ordem especifica, dissociando o disparo de um evento do seu tratamento, permitindo uma melhor usabilidade dos recursos do sistema, visto que o handler de evento pode ser executado de forma simultânea e independente devido a modularidade, reduzindo a necessidade de sincronização.<br> <span class='textSpanPOE1'> Flexibilidade </span>: a programação orientada a eventos permite uma maior flexibilidade e adaptabilidade do programa, visto que as ações são executadas somente os eventos acontecem, possibilitando o programa a responde dinamicamente a diferentes eventos, se adaptando às necessidades do usuário e vontades do programador.<br> <span class='textSpanPOE1'>Adequação para as Interfaces Gráficas:</span> Permite que o usuário utilize o programa sem existe uma sequência predefinida, visto que o usuário possui controle completo sobre as ações que deseja que o programa realize.", 
    "Apesar de possuir bastante vantagens, a programação orientada a eventos não está isenta de desafios, tendo como uma de suas principais desvantagens o seu impacto potencial na capacidade de manutenção do código, visto que programas grandes podem se tornar estruturar complexas caso a modularidade não seja bem aplicada no sistema, isso é chamado de “Callback Hell”, onde o os handler de evento aninhados e retornos de chamada dificultam a compreensão do código.<br> <span class='textSpanPOE1'>Callback Hell:</span> refere-se a um problema predominando presente no desenvolvimento de softwares com programação assíncrona, onde vários retornos de chamada aninhados criam um código complexo.",
    ""
];
const titles = [
    "Programação Orientada a Eventos com Python:",
    "O que é quais as suas Características",
    "Vantagens",
    "Desvantagens",
    "Procurando mais? voce é um verdadeiro nerd curioso"
];

currentTextIndex = 0;

// Seleciona o elemento do texto e botão
const textElement = document.getElementById("textPOE");
const titleElement = document.getElementById("titlePOE");
const nextButton = document.getElementById("btnPOE");

// Função para mudar o texto
function changeText() {
    if (currentTextIndex < texts.length-1) {
        currentTextIndex++;
        titleElement.innerHTML = titles[currentTextIndex];
        textElement.innerHTML = texts[currentTextIndex];
    }

    // Quando o texto for o último, rola para o rodapé
    if (currentTextIndex === texts.length-1) {
        document.getElementById("footer").scrollIntoView({ behavior: "smooth" });
    }

}

// Adiciona o evento de clique ao botão
function changePOE(){
    changeText();
    document.getElementById('clickAudio').play();
}

// Inicializa com o primeiro texto
textElement.innerHTML = texts[currentTextIndex];
titleElement.innerHTML = titles[currentTextIndex];