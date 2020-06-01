/*
Converts inputted string to sentence case

Args:
    theString: Inputted string to be converted
*/
const toSentenceCase = (theString) => {
    const newString = theString.toLowerCase().replace(
        // eslint-disable-next-line
        /(^\s*\w|[\.\!\?]\s*\w)/g,
        (c) => {
            return c.toUpperCase();
        }
    );
    return newString;
};

export { toSentenceCase };
