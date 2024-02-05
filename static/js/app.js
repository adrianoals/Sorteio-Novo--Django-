// document.addEventListener('DOMContentLoaded', function () {
//     // Espera que o DOM esteja completamente carregado

//     // Obtém referências aos elementos HTML
//     var titulo = document.getElementById('titulo');
//     var botaoIniciar = document.getElementById('botao-iniciar');
//     var containerSorteio = document.getElementById('container-sorteio');
//     var formularioPresenca = document.getElementById('formulario-presenca');

//     // Verifica se os elementos foram encontrados
//     if (!titulo || !botaoIniciar || !containerSorteio || !formularioPresenca) {
//         console.log('Um ou mais elementos não foram encontrados');
//         return;
//     }

//     // Adiciona um ouvinte de clique ao botão "Iniciar"
//     botaoIniciar.addEventListener('click', function () {
//         console.log('O botão foi clicado');  // Verifica se o evento de clique está funcionando

//         // Atualiza o conteúdo do <h1> antes de iniciar o sorteio
//         titulo.textContent = 'INICIANDO SORTEIO!';

//         // Altera o conteúdo da div container-sorteio
//         containerSorteio.innerHTML = '<h5 class="mt-3 mb-3 font_subtitle text-dark">LISTA DE PRESENÇA:</h5>';

//         // Torna o formulário de presença visível
//         formularioPresenca.style.display = 'block';
//     });
// });

