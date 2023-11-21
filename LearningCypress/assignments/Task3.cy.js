//Based on the topics discussed, work out the below task:
//· Visit  Swag Labs (saucedemo.com)
describe('Task3', () => {
  it('visit homepage', () => {
    cy.visit('https://www.saucedemo.com/')


/* · Login into application as standard user*/
    cy.get('[data-test="username"]').clear().debug().type("standard_user");
    cy.get('[data-test="password"]').clear().type("secret_sauce");
    cy.get('[data-test="login-button"]').debug().click();


/*· Add any product to cart*/
   cy.get('#add-to-cart-sauce-labs-backpack').click()

/*· Go to shopping cart page*/
   cy.get('.shopping_cart_link').click()

/*· Proceed to checkout */
        cy.get('#checkout').click()

/*· Fill and submit the user details using custom command */

        cy.get('#first-name').clear().type('Shalini')
        cy.get('#last-name').clear().type('Agarwal')
        cy.get('#postal-code').clear().type('123456')
        cy.get('#continue').click()
        cy.get('#finish').click()

/*· Also try .debug() & .pause() to debug the execution
*/
  })
})