context("ResultStore Search", () => {
  beforeEach(() => {
    cy.visit("/");
  });

  it("Should display an error if the query is invalid", () => {
    cy.get('input[id="outlined-adornment-amount"]').type("incorrect query");
    cy.get('p[id="component-error-text"]').contains("Invalid query string.");
  });

  it("Should render the invocations in the table", () => {
    cy.get('input[id="outlined-adornment-amount"]').type(
      "invocation_attributes.users:lewiscraig"
    );
    cy.get('tr[class="MuiTableRow-root MuiTableRow-hover"]').contains(
      "invocations/51be7217-9798-4448-adf8-1e4428c71e9e"
    );
    cy.get('tr[class="MuiTableRow-root MuiTableRow-hover"]').contains(
      "TESTING"
    );
    cy.get('tr[class="MuiTableRow-root MuiTableRow-hover"]').contains(
      "dank,meme"
    );
    cy.get('tr[class="MuiTableRow-root MuiTableRow-hover"]').contains("00:06");
    cy.get('tr[class="MuiTableRow-root MuiTableRow-hover"]').contains(
      "lewiscraig@"
    );
  });

  it("Should display tool1 and tool2 in dropdown and have 1 invocation", () => {
    cy.get('input[id="outlined-adornment-amount"]').type(
      "invocation_attributes.users:lewiscraig"
    );
    cy.get(
      'div[class="MuiSelect-root MuiSelect-select MuiSelect-selectMenu MuiSelect-outlined MuiInputBase-input MuiOutlinedInput-input"]'
    ).click();
    cy.get('ul[class="MuiList-root MuiMenu-list MuiList-padding"]').contains(
      "tool1"
    );
    cy.get('ul[class="MuiList-root MuiMenu-list MuiList-padding"]').contains(
      "tool2"
    );
    cy.get('li[data-value="tool1"]').click();
    cy.get('input[id="outlined-adornment-amount"]').type("i");
    cy.get('tbody[class="MuiTableBody-root"]')
      .find("tr")
      .should("have.length", 1);
  });
});
