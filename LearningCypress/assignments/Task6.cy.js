//const {expect}=require("chai")

describe('api-testing', function(){

    it('GET Request', function(){
        //Visit https://demoqa.com/books
        cy.request('https://demoqa.com/books').then((res) => {
             expect(res.status).to.eq(200)
             })
            //· Write API test for the GET “/BookStore/v1/Books” API
        cy.request('GET','https://demoqa.com/BookStore/v1/books').then((res) => {
          //· Verify Status Code, List of books & Properties.
             expect(res.status).to.eq(200);
             expect(res.body).to.have.property('books').to.be.an('array');
             })





    })
})





/*
· Intercept the response of above API with dummy details

· Verify the API response after stubbing

· Assert the same details in the UI as well.
*/