using System;

class Calculadora
{
    static void Main(string[] args)
    {
        Console.WriteLine("Bem-vindo à calculadora!");

        Console.Write("Digite o primeiro número: ");
        double num1 = double.Parse(Console.ReadLine());

        Console.Write("Digite o segundo número: ");
        double num2 = double.Parse(Console.ReadLine());

        Console.Write("Escolha a operação (+ - * /): ");
        char operacao = char.Parse(Console.ReadLine());

        double resultado = 0.0;
        switch (operacao)
        {
            case '+':
                resultado = num1 + num2;
                break;
            case '-':
                resultado = num1 - num2;
                break;
            case '*':
                resultado = num1 * num2;
                break;
            case '/':
                resultado = num1 / num2;
                break;
            default:
                Console.WriteLine("Operação inválida.");
                break;
        }

        Console.WriteLine($"O resultado é: {resultado}");
    }
}

