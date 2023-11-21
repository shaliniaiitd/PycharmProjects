/*Based on the topics discussed, work out the below task:
Write a custom command to override .type().*/

describe('template spec', () => {
  it('passes', () => {
    cy.visit('https://www.saucedemo.com/').pause();
cy.get('#user-name').type('standard_user', {clear: true});
cy.get('#password').type('secret_sauce', { sensitive: true, clear:true});
cy.get('[data-test="login-button"]').click();

/*· The .type() can accept an option name ‘clear’.

· If option clear is true, then text field should be cleared before enter the given text.

· If option clear is false, then the given text should be entered along with the existing text.

· Default value for the option clear can be ‘false’.

· Example*/

})
})