context("ResultStoreSearch Home Page", () => {
  beforeEach(() => {
    cy.visit("/");
  });

  it("Should display an error if the query is invalid", () => {
    cy.get('input[id="outlined-adornment-amount"]').type("incorrect query");
    cy.get('p[id="search-error"]').contains("Invalid query string");
  });

  it("Should render the invocations in the table", () => {
    cy.get('input[id="outlined-adornment-amount"]').type("a");
    cy.get('div[aria-label="row"]').contains(
      "invocations/51be7217-9798-4448-adf8-1e4428c71e9e"
    );
    cy.get('div[aria-label="row"]').contains("TESTING");
    cy.get('div[aria-label="row"]').contains("dank,meme");
    cy.get('div[aria-label="row"]').contains("00:06");
    cy.get('div[aria-label="row"]').contains("lewiscraig@");
  });

  it("Should display tool1 and tool2 in dropdown and have 1 invocation", () => {
    cy.get('input[id="outlined-adornment-amount"]').type("a");
    cy.get('div[id="tool-select"]').click();
    cy.get('li[data-value="tool1"]').contains("tool1");
    cy.get('li[data-value="tool2"').contains("tool2");
    cy.get('li[data-value="tool2"]').click();
    cy.get('input[id="outlined-adornment-amount"]').type("i");
    cy.get('input[id="outlined-adornment-amount"]').type("i");
    cy.get('div[id="InvocationTable"]')
      .find('div[aria-label="row"]')
      .should("have.length", 1);
  });

  it("Should display tooltip on hover", () => {
    cy.get('svg[aria-label="SearchHelp"').trigger("mouseover");
    cy.get('div[class="MuiTooltip-popper"]').contains(
      'Fields that support equals ("=") restrictions:'
    );
  });

  it("Should open the file modal on row click", () => {
    cy.get('input[id="outlined-adornment-amount"]').type("a");
    cy.get('div[aria-rowindex="1"]').click();
    cy.get('div[id="FileModal"]').should("have.length", 1);
  });

  it("Should render files in the file table", () => {
    cy.get('input[id="outlined-adornment-amount"]').type("a");
    cy.get('div[aria-rowindex="1"]').click();
    cy.get('div[id="InvocationModalRow"]').click();
    cy.get('div[id="FileTable"]').contains("test-file");
  });
});
