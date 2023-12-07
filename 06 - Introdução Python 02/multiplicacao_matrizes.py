def mat_mul (A, B):
    num_linhas_A, num_colunas_A = len(A), len(A[0])
    num_linhas_B, num_colunas_B = len(B), len(B[0])
    assert num_colunas_A == num_linhas_B

    vazio = []
    for linha in range(num_colunas_A):
        # comencando uma nova linha
        vazio.append([])
        for coluna in range(num_colunas_B):
            # Adicionando uma nova coluna na linha
            vazio[linha].append(0)
            for k in range(num_colunas_A):
                vazio[linha][coluna] += A[linha][k] * B[k][coluna]

    return vazio


if __name__ == '__main__':
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[1, 2], [3, 4], [5, 6]]
    print(mat_mul(A, B))
