context("ResultStoreSearch FilePage", () => {
  beforeEach(() => {
    cy.visit(
      "/file?prefix=51be7217-9798-4448-adf8-1e4428c71e9e&fileName=test-file"
    );
  });

  it("Should render a file", () => {
    cy.get("body").contains("Multi Dimensional Table (Plx custom chart chart)");
  });
});
