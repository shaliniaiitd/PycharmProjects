
 /* Task-2:
 * Visit https://www.saucedemo.com/
 */
 describe('template spec', () => {
  it('passes', () => {
    cy.visit('https://www.saucedemo.com/');
 });


 it ('Login into the app by enter the credential', () => {
 cy.get('[data-test="Username"]').clear().type("standard_user");
 cy.get('[data-test="Password"]').clear().type("secret_sauce");
 cy.get('[data-test="login-button"]').click();
 });

 it('Assert the Page Title “Swag Labs”', () => {
 cy.get('.app_logo').should('have.text',"Swag Labs");
 });

 it('Sort the list by “Price (low to high)”.', () => {
 cy.get('data-test="product_sort_contwainer"').select('lohi');
 });

 it ('Add 1st product into the cart', () => {
 cy.get(['data-test="add-to-cart-sauce-labs-onesie"']);
 });

 
 it('Verify the button text changed as “Remove”', () => {
 cy.get(['data-test="remove-sauce-labs-onesie"']).should("have.text","Remove");
 });

 it('Visit shopping cart by click on “Cart” icon at top right', () => {
 /*cy.get(".shopping_cart_link").click().then()*/
 });
})
