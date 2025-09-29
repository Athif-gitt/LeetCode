const checkIfPangram = (sentence) => {
    return new Set(sentence.split("")).size == 26;
}