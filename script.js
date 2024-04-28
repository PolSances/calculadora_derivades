function calculateDerivative() {
    const latexInput = document.getElementById('latexInput').value;

    try {
        // Convert the LaTeX function to a symbolic expression
        const functionExpr = math.parse(latexInput);
        const derivativeExpr = math.derivative(functionExpr, 'x');

        // Display the result
        document.getElementById('result').textContent = `The derivative of the function ${latexInput} with respect to x is: ${derivativeExpr.toString()}.`;
    } catch (error) {
        document.getElementById('result').textContent = 'Error calculating the derivative. Make sure to enter a valid function in LaTeX format.';
    }
}
