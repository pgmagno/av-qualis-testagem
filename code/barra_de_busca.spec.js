/// <reference types="cypress" />

describe('Testa a barra de pesquisa do site Booking.com',() => {
    beforeEach(()=>{
        cy.visit('https://www.booking.com/index.pt-br.html')
        cy.get("#xp__guests__toggle").click();
        for(let i = 0; i < 3; i++) {
            cy.get(".sb-group-children > .bui-stepper > .bui-stepper__wrapper > .bui-stepper__subtract-button").click();
        }
    })

    it('CT-001 - testa a busca por hotéis quando não é inserido um destino',() => {
        cy.get('.sb-searchbox__button').click();
        cy.contains("Por favor, insira um destino para começar a pesquisar.").should('exist');
    });

    it('CT-002 - insere o destino "Rio de Janeiro" no campo de busca, não insere datas e clica em Pesquisar e vai para página de resultados',() => {
        let local = 'Rio de Janeiro';
        cy.get("#ss").type(local);
        cy.get('.sb-searchbox__button').click();
        cy.url().should('include','searchresults');
    });

    it('CT-003 - insere o destino "Rio de Janeiro" no campo de busca, não insere datas e clica em Pesquisar',() => {
        cy.get("#ss").type("Rio de Janeiro");
        cy.get('.sb-searchbox__button').click();
        cy.get("._b61fba663").should('exist');
    });

    it('CT-004 - Pressiona a caixa de seleção de hóspedes',() => {
        cy.get("#xp__guests__toggle").click();
        cy.get("#xp__guests__inputs-container").should("be.visible");
    });
  
    it('CT-005 - insere o destino "Rio de Janeiro", buscando uma data e clica em "Pesquisar"',() => {
        let date = processDate(30);
        cy.get("#ss").type("Rio de Janeiro");
        cy.get(".xp__dates").click();
        cy.get(`[data-date="${date}"]`).click();
        cy.get('.sb-searchbox__button').click();
        cy.get('[data-testid="price-and-discounted-price"]').should('exist');
    });

    it('CT-006 - insere o destino "Rio de Janeiro", buscando uma data (1 dias antes) anterior ao dia de hoje e clica em "Pesquisar"',() => {
        let date = processDate(-1);
        cy.get("#ss").type("Rio de Janeiro");
        cy.get(".xp__dates").click();
        cy.get(`[data-date="${date}"]`).click();
        cy.get('.sb-searchbox__button').click();
        cy.get('[data-testid="price-and-discounted-price"]').should('not.exist');
    });
   
    it('CT-007 - Pressiona o "X" que aparece ao digitar algo no campo de busca',() => {
        cy.get("#ss").type("Rio de Janeiro");
        cy.get('.sb-destination__clear > .bk-icon').click();
        cy.get("#ss").should('contain.text', '');
    });

    it('CT-008 - Testa inserir um número de adultos menor do que 1',() => {
        cy.get("#xp__guests__toggle").click();
        for (let i = 0; i < 5; i++) {
            cy.get(".sb-group__field-adults > .bui-stepper > .bui-stepper__wrapper > .bui-stepper__subtract-button").click();
        }
        cy.get('.sb-group__field-adults > .bui-stepper > .bui-stepper__wrapper > .bui-stepper__display').should('contain.text','1');
    });

    it('CT-009 - Testa inserir um número de adultos maior do que 30',() => {
        cy.get("#xp__guests__toggle").click();
        for (let i = 0; i < 35; i++) {
            cy.get(".sb-group__field-adults > .bui-stepper > .bui-stepper__wrapper > .bui-stepper__add-button").click();
        }
        cy.get('.sb-group__field-adults > .bui-stepper > .bui-stepper__wrapper > .bui-stepper__display').should('contain.text','30');
    });

    it('CT-010 - Testa adicionar uma criança e o campo de idade',() => {
        cy.get("#xp__guests__toggle").click();
        cy.get(".sb-group-children > .bui-stepper > .bui-stepper__wrapper > .bui-stepper__add-button").click();
        for (let i = 0; i < 13; i++) {
            cy.get(".sb-group-children > .bui-stepper > .bui-stepper__wrapper > .bui-stepper__subtract-button").click(); 
        }    
        cy.get(".sb-group-children > .bui-stepper > .bui-stepper__wrapper > .bui-stepper__add-button").click();        
        cy.get('.sb-group-children > .bui-stepper > .bui-stepper__wrapper > .bui-stepper__display').should('contain.text','1');
        cy.get('.sb-group-field-has-error').should('exist');
    });

});

function processDate (numberOfDays) {
    // pega a data de hoje e soma com o número de dias inserido
    // se o número de dias inserido for negativo, o resultado será um dia passado
    // se positivo, um dia futuro
    // o resultado é uma string processada e capaz de ser inserida no elemento data-testeid
    // usado para manipular o calendário da barra de pesquisa

    const today = new Date(); // retorna um objeto com a referente a data de hoje
    const newDate = new Date(); // idem
    newDate.setDate(today.getDate() + numberOfDays); // modifica a data baseado no parâmetro

    let year = newDate.getFullYear(); // salva somente o ano da data nova
    let month = newDate.getMonth() + 1; // salva somente o mês, o intervalo desse method é de 0 a 11, por isso o '+ 1'
    let day = newDate.getDate(); // salva somente o dia

    if (day < 10) {
        day = String("0" + day); // adiciona 0 para formatar corretamente a string
    }                           // para dias com somente um algarismo
    if (month < 10) {           // faz o mesmo para o mês
        month = String("0" + month);
    }
    return `${year}-${month}-${day}`;
}