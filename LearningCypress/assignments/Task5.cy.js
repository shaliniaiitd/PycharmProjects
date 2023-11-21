/*Visit  Swag Labs (saucedemo.com) */
//import  neatCSV from 'neat-csv';

describe('Task5 - fixtures', () => {
    
    
    before(function () {
        cy.fixture('product_details.json').then((data) =>{
        this.product_list = data
        })
    })

    it('passes', function ()  {
    cy.visit('https://www.saucedemo.com/')

/*· Login into application as standard user */
    cy.login("standard_user","secret_sauce")

/*· Add any 3 products to shopping cart */
    cy.get('[class="btn btn_primary btn_small btn_inventory"]').eq(0).click()
    cy.get('[class="btn btn_primary btn_small btn_inventory"]').eq(1).click()
    cy.get('[class="btn btn_primary btn_small btn_inventory"]').eq(2).click()

/*· Go to shopping cart page */
cy.get('#shopping_cart_container').click()

//· Verify the product name and its price using fixtures
//cy.fixture('product_data.json').then(function(products){
// cy.fixture('product_data.csv').then(neatCSV).then((products) => {
//     //let index=0
//     products.forEach((product,index) =>  {
//     cy.get('.inventory_item_name').eq(index).should('have.text',product.name)
//     cy.get('.inventory_item_price').eq(index).should('have.text',product.price)
//     //index = index +1
// })

//     })
   
//· Use this context to invoke the product details

this.product_list.products.forEach((product,index) => {
    cy.get('div.inventory_item_name').eq(index).should('have.text',product.name)
    cy.get('div.inventory_item_price').eq(index).should('have.text',product.price)
})

//· Install Mochawesome and Generate HTML report

// Add npm script in package.json to run the test */


})

  })