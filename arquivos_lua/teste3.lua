-- Função para verificar se um número é primo
function ehPrimo(n)
    if n <= 1 then
        return false
    end
    for i = 2, n - 1 do
        if n % i == 0 then
            return false
        end
    end
    return true
end

-- Função com varargs para somar qualquer quantidade de números
function somaTudo(...)
    local total = 0
    for i = 1, #arg do
        total = total + arg[i]
    end
    return total
end

-- Função que imprime números primos até um limite
function primosAte(limite)
    for i = 1, limite do
        if ehPrimo(i) then
            print("Primo encontrado: " .. i)
        end
    end
end

-- Testes
local a, b = 5, 10
local resultado = somaTudo(a, b, 15, 20)

print("Resultado da soma: " .. resultado)

primosAte(20)

-- Loop com repeat...until
local contador = 1
repeat
    print("Contando até 3: " .. contador)
    contador = contador + 1
until contador > 3