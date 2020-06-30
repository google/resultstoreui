context("ResultStore Search", () => {
  beforeEach(() => {
    cy.visit("/");
  });

  it("Should display an error if the query is invalid", () => {
    cy.get('input[id="outlined-adornment-amount"]').type("incorrect query");
    cy.get('p[id="search-error"]').contains("Invalid query string.");
  });

  it("Should render the invocations in the table", () => {
    cy.get('input[id="outlined-adornment-amount"]').type(
      "invocation_attributes.users:lewiscraig"
    );
    cy.get(
      'div[class="ReactVirtualized__Table__row jss9 jss8 jss10"]'
    ).contains("invocations/51be7217-9798-4448-adf8-1e4428c71e9e");
    cy.get(
      'div[class="ReactVirtualized__Table__row jss9 jss8 jss10"]'
    ).contains("TESTING");
    cy.get(
      'div[class="ReactVirtualized__Table__row jss9 jss8 jss10"]'
    ).contains("dank,meme");
    cy.get(
      'div[class="ReactVirtualized__Table__row jss9 jss8 jss10"]'
    ).contains("00:06");
    cy.get(
      'div[class="ReactVirtualized__Table__row jss9 jss8 jss10"]'
    ).contains("lewiscraig@");
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
    cy.get('li[data-value="tool2"]').click();
    cy.get('input[id="outlined-adornment-amount"]').type("i");
    cy.get('input[id="outlined-adornment-amount"]').type("i");
    cy.get('div[class="ReactVirtualized__Table jss12"]')
      .find('div[class="ReactVirtualized__Table__row jss9 jss8 jss10"]')
      .should("have.length", 1);
  });

  it("Should display tooltip on hover", () => {
    cy.get('svg[aria-label="SearchHelp"').trigger("mouseover");
    cy.get('div[class="MuiTooltip-popper"]').contains(
      'Fields that support equals ("=") restrictions:'
    );
  });
});
