
 /* Task-2: LOCATORS, .then()
 . - class attribute
 # - id attribute
 [data-* = ] css
 * Visit https://www.saucedemo.com/
 */
 describe('template spec', () => {
  it('passes', () => {
    cy.visit('https://www.saucedemo.com/');
    cy.get('[data-test="username"]').clear().type("standard_user");
    cy.get('[data-test="password"]').clear().type("secret_sauce");
    cy.get('[data-test="login-button"]').click();
    cy.get('.app_logo').should('have.text',"Swag Labs");
     cy.get('[data-test="product_sort_container"]').select('lohi');
     cy.get('[data-test="add-to-cart-sauce-labs-onesie"]').click();
     cy.get('#remove-sauce-labs-onesie').should("have.text","Remove");
     let product_name;
     cy.get('.inventory_item_name').eq(0).then(($element) => {
        product_name = $element.text();
        cy.get(".shopping_cart_link").click()
        cy.get(".inventory_item_name").should("have.text",product_name)
        /* · Checkout & Continue without user details */

        cy.get('#checkout').click()
        cy.get('#first-name').clear().type('Shalini')
        cy.get('#last-name').clear().type('Agarwal')
        cy.get('#postal-code').clear().type('123456')
        cy.get('#continue').click()
        cy.get('#finish').click()

        cy.get('.complete-header').should("have.text", 'Thank you for your order!')

        });

 })

 /* · Visit https://www.saucedemo.com/
· Login into the app by enter the credential

· Assert the Page Title “Swag Labs”

· Sort the list by “Price (high to low)”

· Add 1st product into the cart

· Verify the button text changed as “Remove”

· Visit shopping cart by click on “Cart” icon at top right

· Verify Product name by compare with previous page using .then()

· Checkout & Continue without user details

· Verify
 the validation message app
ears after click the continue

*/

 /*('Login into the app by enter the credential', () => {
 cy.get('[data-test="username"]').clear().type("standard_user");
 cy.get('[data-test="password"]').clear().type("secret_sauce");
 cy.get('[data-test="login-button"]').click();
 })

 it('Assert the Page Title “Swag Labs”', () => {
 cy.get('.app_logo').should('have.text',"Swag Labs");
 });

 it('Sort the list by “Price (low to high)”.', () => {
 cy.get('data-test="product_sort_container"').select('lohi');
 });

 it ('Add 1st product into the cart', () => {
 cy.get(['data-test="add-to-cart-sauce-labs-onesie"']);
 });

 
 it('Verify the button text changed as “Remove”', () => {
 cy.get(['data-test="remove-sauce-labs-onesie"']).should("have.text","Remove");
 });


/* it('Visit shopping cart by click on “Cart” icon at top right', () => {
 /*cy.get(".shopping_cart_link").click().then()*/
 /*})*/
})
