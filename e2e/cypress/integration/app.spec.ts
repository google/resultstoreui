context('ResultStore Search', () => {
    beforeEach(() => {
        cy.visit('/');
    });

    it('Should display an error if the query is invalid', () => {
        cy.get('input[id="outlined-adornment-amount"]').type('incorrect query');
        cy.get('p[id="component-error-text"]').contains(
            'Invalid query string.'
        );
    });

    it('Should render the invocations in the table', () => {
        cy.get('input[id="outlined-adornment-amount"]').type(
            'invocation_attributes.users:lewiscraig'
        );
        cy.get('tr[class="MuiTableRow-root MuiTableRow-hover"]').contains(
            'invocations/51be7217-9798-4448-adf8-1e4428c71e9e'
        );
        cy.get('tr[class="MuiTableRow-root MuiTableRow-hover"]').contains(
            'TESTING'
        );
        cy.get('tr[class="MuiTableRow-root MuiTableRow-hover"]').contains(
            'dank,meme'
        );
        cy.get('tr[class="MuiTableRow-root MuiTableRow-hover"]').contains(
            '00:06'
        );
        cy.get('tr[class="MuiTableRow-root MuiTableRow-hover"]').contains(
            'lewiscraig@'
        );
    });
});
