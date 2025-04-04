-- Função que calcula o fatorial de um número
function fatorial(n)
    local resultado = 1
    while n > 1 do
      resultado = resultado * n
      n = n - 1
    end
    return resultado
  end
  
  -- Testa a função com vários valores
  local i = 1
  while i <= 5 do
    print("Fatorial de " .. i .. " é: " .. fatorial(i))
    i = i + 1
  end