import flet as ft
import mysql
import mysql.connector


def conectar_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234',
        database='cooperbuzios'
    )


cooperados = []


def cadastrar_cooperado(vaga, nome, sobrenome):  # função para cadastrar cooperado
    cooperados.append({"vaga": vaga, "nome": nome, "sobrenome": sobrenome})
    conexao = conectar_db()
    cursor = conexao.cursor()

    sql = 'insert into cooperados (vaga, nome, sobrenome) values (%s, %s, %s)'
    valores = (vaga, nome, sobrenome)

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()


def cadastrar_mot_aux(vaga, nome, sobrenome):
    conexao = conectar_db()
    cursor = conexao.cursor()

    sql = 'insert into mot_aux (vaga, nome, sobrenome) values (%s, %s, %s)'
    valores = (vaga, nome, sobrenome)

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()


def cadastrar_fisc(nome, sobrenome, linha):
    conexao = conectar_db()
    cursor = conexao.cursor()

    sql = 'insert into fiscais (nome, sobrenome, linha_principal) values (%s, %s, %s)'
    valores = (nome, sobrenome, linha)

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()


def cadastrar_prancheta1(nome, linha, vaga, nome_m, horario, data):
    conexao = conectar_db()
    cursor = conexao.cursor()
    sql = (
        'insert into prancheta1_vila (nome_f, linha_p, vaga, nome_m, horario, data_) values (%s, %s, %s, %s, %s, %s)')
    valores = (nome, linha, vaga, nome_m, horario, data)
    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()


def cadastrar_prancheta2(nome, linha, vaga, nome_m, horario, data):
    conexao = conectar_db()
    cursor = conexao.cursor()
    sql = ('insert into prancheta2_rasa (nome_f, linha_p, vaga, nome_m, horario, data_) values (%s, %s, %s, %s, %s, %s)')

    valores = (nome, linha, vaga, nome_m, horario, data)
    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()


def fetch_data_c():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234',
        database='cooperbuzios'
    )

    cursor = conexao.cursor()
    cursor.execute('select vaga, nome, sobrenome from cooperados')

    resultado = cursor.fetchall()

    cursor.close()
    conexao.close()
    return resultado


def fetch_data_mot():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234',
        database='cooperbuzios'
    )

    cursor = conexao.cursor()
    cursor.execute('select vaga, nome, sobrenome from mot_aux')
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado


def fetch_data_fiscais():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234',
        database='cooperbuzios'
    )

    cursor = conexao.cursor()
    cursor.execute('select nome, sobrenome, linha_principal from fiscais')
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado


def atualizar_coop():
    conexao = conectar_db()
    cursor = conexao.cursor()
    cursor.execute('select id, vaga, nome, sobrenome from cooperados')
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado


def atualizar_mot_aux():
    conexao = conectar_db()
    cursor = conexao.cursor()
    cursor.execute('select id, vaga, nome, sobrenome from mot_aux')
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado


def atualizar_fisc():
    conexao = conectar_db()
    cursor = conexao.cursor()
    cursor.execute('select nome, sobrenome, linha_principal from fiscais')
    resultado = cursor.fetchall()

    cursor.close()
    conexao.cursor()

    return resultado


def atualizar_vilaXcentro():
    conexao = conectar_db()
    cursor = conexao.cursor()
    cursor.execute(
        'select id, nome_f, linha_p, vaga, nome_m, horario, data_ from prancheta1_vila order by id desc')
    resultado = cursor.fetchall()

    cursor.close()
    conexao.close()

    return resultado


def atualizar_rasaXcentro():
    conexao = conectar_db()
    cursor = conexao.cursor()
    cursor.execute(
        'select id,  nome_f, linha_p, vaga, nome_m, horario, data_ from prancheta2_rasa')
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado


def main(page: ft.Page):

    page.scroll = ft.ScrollMode.AUTO
    page.scroll = ft.ScrollMode.HIDDEN
    data_c = fetch_data_c()

    dt_c = ft.Container(
        content=ft.Row(
            controls=[
                ft.DataTable(
                    columns=[
                        ft.DataColumn(label=ft.Text('Vaga')),
                        ft.DataColumn(label=ft.Text('Nome')),
                        ft.DataColumn(label=ft.Text('Sobrenome'))
                    ],
                    rows=[
                        ft.DataRow(
                            cells=[
                                ft.DataCell(content=ft.Text(str(vaga))),
                                ft.DataCell(content=ft.Text(nome)),
                                ft.DataCell(content=ft.Text(sobrenome))
                            ]
                        )for vaga, nome, sobrenome in data_c
                    ],
                    divider_thickness=1,
                    vertical_lines=ft.BorderSide(
                        width=2, color=ft.Colors.AMBER),
                    horizontal_lines=ft.BorderSide(
                        width=2, color=ft.Colors.AMBER),
                    border=ft.border.all(width=2, color=ft.Colors.AMBER),
                    border_radius=ft.border_radius.all(5),
                    data_row_color=ft.Colors.GREY,
                    heading_row_color=ft.Colors.BLUE_900

                )
            ]
        )
    )

    data_mot = fetch_data_mot()

    dt_mot = ft.Container(
        content=ft.Row(
            controls=[
                ft.DataTable(
                    columns=[
                        ft.DataColumn(label=ft.Text('Vaga')),
                        ft.DataColumn(label=ft.Text('Nome')),
                        ft.DataColumn(label=ft.Text('Sobrenome'))
                    ],
                    rows=[
                        ft.DataRow(
                            cells=[
                                ft.DataCell(content=ft.Text(str(vaga))),
                                ft.DataCell(content=ft.Text(nome)),
                                ft.DataCell(content=ft.Text(sobrenome))
                            ]
                        )for vaga, nome, sobrenome in data_mot
                    ],
                    divider_thickness=1,
                    vertical_lines=ft.BorderSide(
                        width=2, color=ft.Colors.AMBER),
                    horizontal_lines=ft.BorderSide(
                        width=2, color=ft.Colors.AMBER),
                    border=ft.border.all(width=2, color=ft.Colors.AMBER),
                    border_radius=ft.border_radius.all(5),
                    data_row_color=ft.Colors.GREY,
                    heading_row_color=ft.Colors.BLUE_900

                )
            ]
        )
    )

    data_fisc = fetch_data_fiscais()
    dt_fisc = ft.Container(
        content=ft.Row(
            controls=[
                ft.DataTable(
                    columns=[
                        ft.DataColumn(label=ft.Text('Nome')),
                        ft.DataColumn(label=ft.Text('Sobrenome')),
                        ft.DataColumn(label=ft.Text('Linha Principal'))
                    ],
                    rows=[
                        ft.DataRow(
                            cells=[
                                ft.DataCell(content=ft.Text(nome)),
                                ft.DataCell(content=ft.Text(sobrenome)),
                                ft.DataCell(content=ft.Text(linha_p))
                            ]
                        )for nome, sobrenome, linha_p in data_fisc
                    ],
                    divider_thickness=1,
                    vertical_lines=ft.BorderSide(
                        width=2, color=ft.Colors.AMBER),
                    horizontal_lines=ft.BorderSide(
                        width=2, color=ft.Colors.AMBER),
                    border=ft.border.all(width=2, color=ft.Colors.AMBER),
                    border_radius=ft.border_radius.all(5),
                    data_row_color=ft.Colors.GREY,
                    heading_row_color=ft.Colors.BLUE_900
                )
            ]
        )
    )
    global vaga_c, nome_c, sobrenome_c

    def toggle_select(e):
        e.control.selected = not e.control.selected
        e.control.update()

    def atualizar_c():  # o código aparentemente está atualizando corretamente
        # dt1.content.controls.clear()

        def delete_c(e):

           # Get selected rows from the DataTable
            selected_rows = [
                vaga for vaga in row.content.controls[0].rows if vaga.selected]

            if not selected_rows:
                # Optional: Show an alert if no row is selected
                page.open(ft.SnackBar(content=ft.Text(
                    "Por favor, selecione um cooperado para deletar")))
                return

            # Get the vaga (which seems to be your identifier) from the selected row
            selected_vaga = selected_rows[0].cells[0].content.value

            try:
                # Create connection and cursor
                conexao = conectar_db()
                cursor = conexao.cursor()

                # Execute delete query using vaga as identifier
                cursor.execute('DELETE FROM cooperados WHERE id = %s',
                               (selected_vaga,))
                conexao.commit()

                # Close cursor and connection
                cursor.close()
                conexao.close()

                # Optional: Show success message
                page.open(ft.SnackBar(
                    content=ft.Text("Cooperado deletado com sucesso!")))

                # Update the table after deletion
                atualizar_c()

            except Exception as e:
                # Optional: Show error message
                page.open(ft.SnackBar(
                    content=ft.Text(f"Erro ao deletar: {str(e)}")))
                print(f"Erro ao deletar cooperado: {str(e)}")
        page.clean()

        def fechar(e):
            atualizado.content.controls.clear()

            page.add(p)
            page.update()

        def salvar_c(e):
            vaga = vaga_c.value
            nome = nome_c.value
            sobrenome = sobrenome_c.value
            cadastrar_cooperado(vaga, nome, sobrenome)

            atualizar_c()

        def atualizar_coop():
            conexao = conectar_db()
            cursor = conexao.cursor()
            cursor.execute('select id, vaga, nome, sobrenome from cooperados')
            resultado = cursor.fetchall()
            cursor.close()
            conexao.close()
            return resultado

        dado_c = atualizar_coop()
        vaga_c = ft.TextField(label='Vaga do Cooperado', width=200, height=30, text_size=14, border_radius=ft.border_radius.all(
            30), border_color=ft.Colors.AMBER, color=ft.Colors.WHITE, label_style=ft.TextStyle(size=12), col={'xs': 12, 'sm': 2})
  # fase de texte

        nome_c = ft.TextField(label='Nome do Cooperado', width=200, height=30, text_size=14, border_radius=ft.border_radius.all(
            30), border_color=ft.Colors.AMBER, color=ft.Colors.WHITE, label_style=ft.TextStyle(size=12), col={'xs': 12, 'sm': 2})
 # fase de texte

        sobrenome_c = ft.TextField(label='Sobrenome do Cooperado', width=200, height=30, text_size=14, border_radius=ft.border_radius.all(
            30), border_color=ft.Colors.AMBER, color=ft.Colors.WHITE, label_style=ft.TextStyle(size=12), col={'xs': 12, 'sm': 2})
  # fase de texte

        row = ft.Container(
            content=ft.ResponsiveRow(
                controls=[
                    ft.DataTable(
                        columns=[
                            ft.DataColumn(label=ft.Text('Id', col={
                                'xs': 12, 'sm': 1}, size=10), heading_row_alignment=ft.MainAxisAlignment.START),
                            ft.DataColumn(label=ft.Text('Vaga', col={
                                          'xs': 12, 'sm': 1}, size=10), heading_row_alignment=ft.MainAxisAlignment.START),
                            ft.DataColumn(label=ft.Text('Nome', col={
                                          'xs': 12, 'sm': 1}, size=10), heading_row_alignment=ft.MainAxisAlignment.START),
                            ft.DataColumn(label=ft.Text('Sobrenome', col={
                                          'xs': 12, 'sm': 1}, size=10), heading_row_alignment=ft.MainAxisAlignment.START)
                        ],
                        rows=[
                            ft.DataRow(
                                cells=[
                                    ft.DataCell(content=ft.Text(
                                        id, col={'xs': 12, 'sm': 1}, size=10)),
                                    ft.DataCell(content=ft.Text(
                                        str(vaga), col={'xs': 12, 'sm': 1}, size=10)),
                                    ft.DataCell(content=ft.Text(
                                        nome, col={'xs': 12, 'sm': 1}, size=10)),
                                    ft.DataCell(content=ft.Text(
                                        sobrenome, col={'xs': 12, 'sm': 1}, size=10)),
                                ],
                                selected=False,
                                on_select_changed=toggle_select,
                                data=0

                            )for id, vaga, nome, sobrenome in dado_c


                        ],
                        divider_thickness=1,
                        vertical_lines=ft.BorderSide(
                            width=2, color=ft.Colors.AMBER),
                        horizontal_lines=ft.BorderSide(
                            width=2, color=ft.Colors.AMBER),
                        border=ft.border.all(
                            width=2, color=ft.Colors.AMBER),
                        border_radius=ft.border_radius.all(5),
                        # data_row_color=ft.Colors.BLACK,
                        heading_row_color=ft.Colors.BLUE_900,
                        show_checkbox_column=False,
                        column_spacing=10
                    )
                ]
            )
        )

        atualizado = ft.Container(
            content=ft.ResponsiveRow(
                controls=[
                    ft.ResponsiveRow(
                        controls=[
                            ft.ElevatedButton("Informações os Cooperados", bgcolor=ft.Colors.AMBER, color=ft.Colors.BLACK, width=250, col={
                                              'xs': 4, 'sm': 3}, style=ft.ButtonStyle(text_style=ft.TextStyle(size=12, weight=ft.FontWeight.BOLD))),
                            ft.ElevatedButton(
                                text='Cadastrar', on_click=salvar_c, bgcolor=ft.Colors.GREEN, color=ft.Colors.BLACK, width=100, col={'xs': 3, 'sm': 3}, style=ft.ButtonStyle(text_style=ft.TextStyle(size=12, weight=ft.FontWeight.BOLD))),
                            ft.ElevatedButton(
                                text='Deletar', color=ft.Colors.BLACK, bgcolor=ft.Colors.RED, width=100, on_click=delete_c, col={'xs': 3, 'sm': 3}, style=ft.ButtonStyle(text_style=ft.TextStyle(size=12, weight=ft.FontWeight.BOLD))),
                            ft.Container(col={'xs': 0, 'sm': 2}),
                            ft.IconButton(
                                icon=ft.Icons.CLOSE, icon_color=ft.Colors.RED, on_click=fechar, col={'xs': 1, 'sm': 1}, style=ft.ButtonStyle(text_style=ft.TextStyle(size=12, weight=ft.FontWeight.BOLD)))
                        ]
                    ),
                    ft.Container(content=ft.ResponsiveRow(controls=[
                        vaga_c,
                        nome_c,
                        sobrenome_c
                    ]
                    )
                    ),
                    row
                ],
                vertical_alignment=ft.CrossAxisAlignment.START
            )

        )
        page.add(atualizado)

        page.update()

    def salvar_c(e):
        vaga = vaga_c.value
        nome = nome_c.value
        sobrenome = sobrenome_c.value
        cadastrar_cooperado(vaga, nome, sobrenome)
        atualizar_c()

    vaga_c = ft.TextField(label='Vaga do Cooperado', text_size=16, width=200, border_radius=ft.border_radius.all(
        30), border_color=ft.Colors.AMBER, color=ft.Colors.WHITE)  # fase de texte

    nome_c = ft.TextField(label='Nome do Cooperado', text_size=16, width=200, border_radius=ft.border_radius.all(
        30), border_color=ft.Colors.AMBER, color=ft.Colors.WHITE)  # fase de texte

    sobrenome_c = ft.TextField(label='Sobrenome do Cooperado', text_size=16, width=200, border_radius=ft.border_radius.all(
        30), border_color=ft.Colors.AMBER, color=ft.Colors.WHITE)  # fase de texte

    def dt_cooperados(e):
        atualizar_c()

    def salvar_m_a(e):
        vaga = vaga_m_a.value
        nome = nome_m_a.value
        sobrenome = sobrenome_m_a.value
        cadastrar_mot_aux(vaga, nome, sobrenome)

    global vaga_m_a, nome_m_a, sobrenome_m_a
    vaga_m_a = ft.TextField(label='Vaga do Cooperado', width=200, height=30, text_size=14, border_radius=ft.border_radius.all(
        # fase de texte
        30), border_color=ft.Colors.AMBER, color=ft.Colors.WHITE, label_style=ft.TextStyle(size=12), col={'xs': 12, 'sm': 2})

    nome_m_a = ft.TextField(label='Nome do Motorista', width=200, height=30, text_size=14, border_radius=ft.border_radius.all(
        # fase de texte
        30), border_color=ft.Colors.AMBER, color=ft.Colors.WHITE, label_style=ft.TextStyle(size=12), col={'xs': 12, 'sm': 2})

    sobrenome_m_a = ft.TextField(label='Sobrenome do Motorista', width=200, height=30, text_size=14, border_radius=ft.border_radius.all(
        # fase de texte
        30), border_color=ft.Colors.AMBER, color=ft.Colors.WHITE, label_style=ft.TextStyle(size=12), col={'xs': 12, 'sm': 2})

    def atualizar_m_a():
        # dt2.content.controls.clear()

        def delete_m_a(e):
            selected_mot = [
                nome for nome in row2.content.controls[0].rows if nome.selected
            ]

            if not selected_mot:
                page.open(ft.SnackBar(content=ft.Text(
                    "Por favor, selecione um cooperado para deletar")))
                return

            selected_vaga = selected_mot[0].cells[0].content.value

            try:
                conexao = conectar_db()
                cursor = conexao.cursor()

                cursor.execute(
                    'DELETE FROM mot_aux WHERE id = %s', (selected_vaga,))

                conexao.commit()

                cursor.close()
                conexao.close()
                page.open(ft.SnackBar(
                    ft.Text("Motorista auxiliar deletado com sucesso!")))

                atualizar_m_a()

            except:
                page.open(ft.SnackBar(ft.Text(f"Erro ao deletar: {str(e)}")))

        page.clean()

        def fechar(e):
            atualizado.content.controls.clear()
            page.add(p)
            page.update()

        def salvar_m_a(e):
            vaga = vaga_m_a.value
            nome = nome_m_a.value
            sobrenome = sobrenome_m_a.value
            cadastrar_mot_aux(vaga, nome, sobrenome)
            atualizar_m_a()
        dado_m = atualizar_mot_aux()
        row2 = ft.Container(
            content=ft.ResponsiveRow(
                controls=[
                    ft.DataTable(
                        columns=[
                            ft.DataColumn(label=ft.Text('Id', col={
                                          'xs': 12, 'sm': 1}, size=10), heading_row_alignment=ft.MainAxisAlignment.START),
                            ft.DataColumn(label=ft.Text('Vaga', col={
                                          'xs': 12, 'sm': 1}, size=10), heading_row_alignment=ft.MainAxisAlignment.START),
                            ft.DataColumn(label=ft.Text('Nome', col={
                                          'xs': 12, 'sm': 1}, size=10), heading_row_alignment=ft.MainAxisAlignment.START),
                            ft.DataColumn(label=ft.Text('Sobrenome', col={
                                          'xs': 12, 'sm': 1}, size=10), heading_row_alignment=ft.MainAxisAlignment.START)
                        ],
                        rows=[
                            ft.DataRow(
                                cells=[
                                    ft.DataCell(content=ft.Text(
                                        id, col={'xs': 12, 'sm': 1}, size=10)),
                                    ft.DataCell(content=ft.Text(
                                        str(vaga), col={'xs': 12, 'sm': 1}, size=10)),
                                    ft.DataCell(content=ft.Text(
                                        nome, col={'xs': 12, 'sm': 1}, size=10)),
                                    ft.DataCell(content=ft.Text(
                                        sobrenome, col={'xs': 12, 'sm': 1}, size=10)),

                                ],
                                selected=False,
                                on_select_changed=toggle_select,
                                data=0
                            )for id, vaga, nome, sobrenome in dado_m
                        ],
                        divider_thickness=1,
                        vertical_lines=ft.BorderSide(
                            width=2, color=ft.Colors.AMBER),
                        horizontal_lines=ft.BorderSide(
                            width=2, color=ft.Colors.AMBER),
                        border=ft.border.all(width=2, color=ft.Colors.AMBER),
                        border_radius=ft.border_radius.all(5),
                        # data_row_color=ft.Colors.BLACK,
                        heading_row_color=ft.Colors.BLUE_900,
                        column_spacing=10

                    )
                ]
            )
        )

        atualizado = ft.Container(content=ft.ResponsiveRow(
            controls=[
                ft.ResponsiveRow(
                    controls=[
                        ft.ElevatedButton("Informações os Cooperados", bgcolor=ft.Colors.AMBER, color=ft.Colors.BLACK, width=250, col={
                            'xs': 4, 'sm': 3}, style=ft.ButtonStyle(text_style=ft.TextStyle(size=12, weight=ft.FontWeight.BOLD))),
                        ft.ElevatedButton(
                            text='Cadastrar', on_click=salvar_m_a, bgcolor=ft.Colors.GREEN, color=ft.Colors.BLACK, width=100, col={'xs': 3, 'sm': 3}, style=ft.ButtonStyle(text_style=ft.TextStyle(size=12, weight=ft.FontWeight.BOLD))),
                        ft.ElevatedButton(
                            text='Deletar', color=ft.Colors.BLACK, bgcolor=ft.Colors.RED, width=100, on_click=delete_m_a, col={'xs': 3, 'sm': 3}, style=ft.ButtonStyle(text_style=ft.TextStyle(size=12, weight=ft.FontWeight.BOLD))),
                        ft.Container(col={'xs': 0, 'sm': 2}),
                        ft.IconButton(
                            icon=ft.Icons.CLOSE, icon_color=ft.Colors.RED, on_click=fechar, col={'xs': 1, 'sm': 1}, style=ft.ButtonStyle(text_style=ft.TextStyle(size=12, weight=ft.FontWeight.BOLD)))
                    ]
                ),
                ft.Container(content=ft.ResponsiveRow(controls=[
                    vaga_m_a,
                    nome_m_a,
                    sobrenome_m_a,
                ]
                )
                ),
                row2
            ],
            vertical_alignment=ft.CrossAxisAlignment.START

        )
        )
        # dt2.content.controls.append(atualizado)
        page.add(atualizado)

    def dt_mot_aux(e):

        atualizar_m_a()

    global nome_fisc, sobrenome_fisc, linha_fisc
    nome_fisc = ft.TextField(label='Nome do Fiscal', width=200, height=30, text_size=14, border_radius=ft.border_radius.all(
        # fase de texte
        30), border_color=ft.Colors.AMBER, color=ft.Colors.WHITE, label_style=ft.TextStyle(size=12), col={'xs': 12, 'sm': 2})

    sobrenome_fisc = ft.TextField(label='Sobrenome do Fiscal', width=200, height=30, text_size=14, border_radius=ft.border_radius.all(
        # fase de texte
        30), border_color=ft.Colors.AMBER, color=ft.Colors.WHITE, label_style=ft.TextStyle(size=12), col={'xs': 12, 'sm': 2})

    linha_fisc = ft.TextField(label='Linha Principal', width=200, height=30, text_size=14, border_radius=ft.border_radius.all(
        # fase de texte
        30), border_color=ft.Colors.AMBER, color=ft.Colors.WHITE, label_style=ft.TextStyle(size=12), col={'xs': 12, 'sm': 2})

    def atualizar_fiscal():
        '''dt3.content.controls.clear()'''

        def deletar_fiscal(e):
            selected_fiscal = [
                fiscal for fiscal in row3.content.controls[0].rows if fiscal.selected
            ]

            if not selected_fiscal:
                page.open(ft.SnackBar(
                    ft.Text("Selecione um Fiscal para deletar!")))

            # explicando o codigo: selecionando a primeira linha da variavel 'selected_fiscal' --> [0]. depois está sendo selecionado a primeira célula da linha. depos um '.content.value' para puxar o valor
            selected_nome = selected_fiscal[0].cells[0].content.value

            try:
                conexao = conectar_db()
                cursor = conexao.cursor()

                cursor.execute(
                    "DELETE FROM fiscais WHERE nome=%s", (selected_nome,))
                conexao.commit()

                cursor.close()
                conexao.close()
                page.open(ft.SnackBar(ft.Text("Fiscal deltado com sucesso!")))

                atualizar_fiscal()

            except:
                page.open(ft.SnackBar(ft.Text("Erro ao deletar Fiscal!")))
        page.clean()
        dado_f = atualizar_fisc()

        def fechar(e):
            atualizado.content.controls.clear()
            page.add(p)
            page.update()

        def salvar_fisc(e):
            nome = nome_fisc.value
            sobrenome = sobrenome_fisc.value
            linha = linha_fisc.value

            cadastrar_fisc(nome, sobrenome, linha)
            atualizar_fiscal()
        row3 = ft.Container(
            content=ft.ResponsiveRow(
                controls=[ft.DataTable(
                    columns=[
                        ft.DataColumn(label=ft.Text('Nome', col={
                            'xs': 12, 'sm': 1}, size=10), heading_row_alignment=ft.MainAxisAlignment.START),
                        ft.DataColumn(label=ft.Text('Sobrenome', col={
                            'xs': 12, 'sm': 1}, size=10), heading_row_alignment=ft.MainAxisAlignment.START),
                        ft.DataColumn(label=ft.Text('Linha Principal', col={
                            'xs': 12, 'sm': 1}, size=10), heading_row_alignment=ft.MainAxisAlignment.START)
                    ],
                    rows=[
                        ft.DataRow(
                            cells=[
                                ft.DataCell(content=ft.Text(
                                    nome, col={'xs': 12, 'sm': 1}, size=10)),
                                ft.DataCell(content=ft.Text(
                                    sobrenome, col={'xs': 12, 'sm': 1}, size=10)),
                                ft.DataCell(content=ft.Text(
                                    linha, col={'xs': 12, 'sm': 1}, size=10))
                            ],
                            selected=False,
                            on_select_changed=toggle_select,
                            data=0
                        ) for nome, sobrenome, linha in dado_f
                    ],
                    divider_thickness=1,
                    vertical_lines=ft.BorderSide(
                        width=2, color=ft.Colors.AMBER),
                    horizontal_lines=ft.BorderSide(
                        width=2, color=ft.Colors.AMBER),
                    border=ft.border.all(width=2, color=ft.Colors.AMBER),
                    border_radius=ft.border_radius.all(5),
                    # data_row_color=ft.Colors.GREY,
                    heading_row_color=ft.Colors.BLUE_900,
                    column_spacing=10
                )
                ]
            )
        )

        atualizado = ft.Container(content=ft.ResponsiveRow(
            controls=[
                ft.ResponsiveRow(
                    controls=[
                        ft.ElevatedButton("Informações os Fiscais", bgcolor=ft.Colors.AMBER, color=ft.Colors.BLACK, width=250, col={
                            'xs': 4, 'sm': 3}, style=ft.ButtonStyle(text_style=ft.TextStyle(size=12, weight=ft.FontWeight.BOLD))),
                        ft.ElevatedButton(
                            text='Cadastrar', on_click=salvar_fisc, bgcolor=ft.Colors.GREEN, color=ft.Colors.BLACK, width=100, col={'xs': 3, 'sm': 3}, style=ft.ButtonStyle(text_style=ft.TextStyle(size=12, weight=ft.FontWeight.BOLD))),
                        ft.ElevatedButton(
                            text='Deletar', color=ft.Colors.BLACK, bgcolor=ft.Colors.RED, width=100, on_click=deletar_fiscal, col={'xs': 3, 'sm': 3}, style=ft.ButtonStyle(text_style=ft.TextStyle(size=12, weight=ft.FontWeight.BOLD))),
                        ft.Container(col={'xs': 0, 'sm': 2}),
                        ft.IconButton(
                            icon=ft.Icons.CLOSE, icon_color=ft.Colors.RED, on_click=fechar, col={'xs': 1, 'sm': 1}, style=ft.ButtonStyle(text_style=ft.TextStyle(size=12, weight=ft.FontWeight.BOLD)))
                    ]
                ),
                ft.Container(content=ft.ResponsiveRow(controls=[
                    nome_fisc,
                    sobrenome_fisc,
                    linha_fisc,
                ]
                )
                ),
                row3
            ],
            vertical_alignment=ft.CrossAxisAlignment.START
        )
        )
        page.add(atualizado)
        page.update()

    def dt_fiscais(e):

        atualizar_fiscal()

    global nome_f, linha_p, vaga_m, horario, data_

    nome_f = ft.TextField(label='Nome do Fiscal', width=200, height=30, text_size=14, border_radius=ft.border_radius.all(
        30), border_color=ft.Colors.AMBER, color=ft.Colors.WHITE, label_style=ft.TextStyle(size=12), col={'xs': 12, 'sm': 2})

    linha_p = ft.TextField(label='Linha Principal', width=200, height=30, text_size=14, border_radius=ft.border_radius.all(
        30), border_color=ft.Colors.AMBER, color=ft.Colors.WHITE, label_style=ft.TextStyle(size=12), col={'xs': 12, 'sm': 2})

    vaga_m = ft.TextField(label='Vaga', width=200, height=30, text_size=14, border_radius=ft.border_radius.all(
        30), border_color=ft.Colors.AMBER, color=ft.Colors.WHITE, label_style=ft.TextStyle(size=12), col={'xs': 12, 'sm': 2})

    nome_m = ft.TextField(label='Nome do Motorista', width=200, height=30, text_size=14, border_radius=ft.border_radius.all(
        30), border_color=ft.Colors.AMBER, color=ft.Colors.WHITE, label_style=ft.TextStyle(size=12), col={'xs': 12, 'sm': 2})

    horario = ft.TextField(label='Horario de Saída', width=200, height=30, text_size=14, border_radius=ft.border_radius.all(
        30), border_color=ft.Colors.AMBER, color=ft.Colors.WHITE, label_style=ft.TextStyle(size=12), col={'xs': 12, 'sm': 2})

    data_ = ft.TextField(label='Data', width=200, height=30, text_size=14, border_radius=ft.border_radius.all(
        30), border_color=ft.Colors.AMBER, color=ft.Colors.WHITE, label_style=ft.TextStyle(size=12), col={'xs': 12, 'sm': 2})

    def atualizar_prancheta1():
        def deletar_prancheta1(e):
            selected_row = [
                linha for linha in row4.content.controls[0].rows if linha.selected
            ]

            if not selected_row:
                page.open(ft.SnackBar(content=ft.Text(
                    'Por favor selecione um ítem para deletar!')))

            selected_cell = selected_row[0].cells[0].content.value

            try:
                conexao = conectar_db()
                cursor = conexao.cursor()

                cursor.execute(
                    'delete from prancheta1_vila where id=%s', (selected_cell,))
                cursor.fetchall()
                conexao.commit()

                cursor.close()
                conexao.close()
                atualizar_prancheta1()

            except:
                page.open(ft.SnackBar(content=ft.Text('Algo eu Errado!')))

        def fechar(e):
            atualizado.content.controls.clear()
            page.add(p)
            page.update()

        def salvar_prancheta(e):
            nome = nome_f.value
            linha = linha_p.value
            vaga = vaga_m.value
            nome_ = nome_m.value
            hora = horario.value
            data = data_.value
            cadastrar_prancheta1(nome, linha, vaga, nome_, hora, data)
            atualizar_prancheta1()
        page.clean()

        global dado_prancheta
        dado_prancheta = atualizar_vilaXcentro()
        row4 = ft.Container(
            content=ft.ResponsiveRow(
                controls=[
                    ft.DataTable(
                        columns=[
                            ft.DataColumn(label=ft.Text(
                                'Id', col={'xs': 12, 'sm': 1}, size=10), heading_row_alignment=ft.MainAxisAlignment.START),
                            ft.DataColumn(label=ft.Text(
                                'Nome do Fiscal', col={'xs': 12, 'sm': 1}, size=10), heading_row_alignment=ft.MainAxisAlignment.START),
                            ft.DataColumn(
                                label=ft.Text('Linha Principal', col={'xs': 12, 'sm': 1}, size=10), heading_row_alignment=ft.MainAxisAlignment.START),
                            ft.DataColumn(label=ft.Text(
                                'Vaga', col={'xs': 12, 'sm': 1}, size=10), heading_row_alignment=ft.MainAxisAlignment.START),
                            ft.DataColumn(label=ft.Text(
                                'Nome do Motorista', col={'xs': 12, 'sm': 1}, size=10), heading_row_alignment=ft.MainAxisAlignment.START),
                            ft.DataColumn(label=ft.Text(
                                'Horario de Saída', col={'xs': 12, 'sm': 1}, size=10), heading_row_alignment=ft.MainAxisAlignment.START),
                            ft.DataColumn(label=ft.Text(
                                'Data', col={'xs': 12, 'sm': 1}, size=10), heading_row_alignment=ft.MainAxisAlignment.START)
                        ],
                        rows=[ft.DataRow(
                            cells=[
                                ft.DataCell(content=ft.Text(
                                    id, col={'xs': 12, 'sm': 1}, size=10)),
                                ft.DataCell(content=ft.Text(
                                    nome, col={'xs': 12, 'sm': 1}, size=10)),
                                ft.DataCell(content=ft.Text(
                                    linha, col={'xs': 12, 'sm': 1}, size=10)),
                                ft.DataCell(content=ft.Text(
                                    vaga, col={'xs': 12, 'sm': 1}, size=10)),
                                ft.DataCell(content=ft.Text(
                                    nome_m, col={'xs': 12, 'sm': 1}, size=10)),
                                ft.DataCell(content=ft.Text(
                                    horario, col={'xs': 12, 'sm': 1}, size=10)),
                                ft.DataCell(content=ft.Text(
                                    data, col={'xs': 12, 'sm': 1}, size=10))
                            ],
                            selected=False,
                            on_select_changed=toggle_select,
                            data=0
                        ) for id, nome, linha, vaga, nome_m, horario, data in dado_prancheta
                        ],
                        divider_thickness=1,
                        vertical_lines=ft.BorderSide(
                            width=2, color=ft.Colors.AMBER),
                        horizontal_lines=ft.BorderSide(
                            width=2, color=ft.Colors.AMBER),
                        border=ft.border.all(width=2, color=ft.Colors.AMBER),
                        border_radius=ft.border_radius.all(5),
                        # data_row_color=ft.Colors.GREY,
                        heading_row_color=ft.Colors.BLUE_900,
                        column_spacing=10
                    )

                ]
            )
        )
        atualizado = ft.Container(
            content=ft.ResponsiveRow(
                controls=[
                    ft.ResponsiveRow(
                        controls=[
                            ft.ElevatedButton("Prancheta Vila Verde X Centro", bgcolor=ft.Colors.AMBER, color=ft.Colors.BLACK, width=250, col={
                                              'xs': 4, 'sm': 3}, style=ft.ButtonStyle(text_style=ft.TextStyle(size=12, weight=ft.FontWeight.BOLD))),
                            ft.ElevatedButton(
                                text='Cadastrar', on_click=salvar_prancheta, bgcolor=ft.Colors.GREEN, color=ft.Colors.BLACK, width=100, col={'xs': 3, 'sm': 3}, style=ft.ButtonStyle(text_style=ft.TextStyle(size=12, weight=ft.FontWeight.BOLD))),
                            ft.ElevatedButton(
                                text='Deletar', color=ft.Colors.BLACK, bgcolor=ft.Colors.RED, width=100, on_click=deletar_prancheta1, col={'xs': 3, 'sm': 3}, style=ft.ButtonStyle(text_style=ft.TextStyle(size=12, weight=ft.FontWeight.BOLD))),
                            ft.Container(col={'xs': 0, 'sm': 2}),
                            ft.IconButton(
                                icon=ft.Icons.CLOSE, icon_color=ft.Colors.RED, on_click=fechar, col={'xs': 1, 'sm': 1}, style=ft.ButtonStyle(text_style=ft.TextStyle(size=12, weight=ft.FontWeight.BOLD)))
                        ]

                    ),
                    ft.Container(content=ft.ResponsiveRow(controls=[
                        nome_f,
                        linha_p,
                        vaga_m,
                        nome_m,
                        horario,
                        data_
                    ]
                    )
                    ),
                    row4

                ]
            )
        )
        page.add(atualizado)
        page.update()

    def dt_pranchetas1(e):
        atualizar_prancheta1()

    global nome_f2, linha_p2, vaga_m2, horario2, data_2

    nome_f2 = ft.TextField(label='Nome do Fiscal', width=200, height=30, text_size=12, border_radius=ft.border_radius.all(
        30), border_color=ft.Colors.AMBER, color=ft.Colors.WHITE, label_style=ft.TextStyle(size=12), col={'xs': 12, 'sm': 2})

    linha_p2 = ft.TextField(label='Linha Principal', width=200, height=30, text_size=12, border_radius=ft.border_radius.all(
        30), border_color=ft.Colors.AMBER, color=ft.Colors.WHITE, label_style=ft.TextStyle(size=12), col={'xs': 12, 'sm': 2})

    vaga_m2 = ft.TextField(label='Vaga', width=200, height=30, text_size=12, border_radius=ft.border_radius.all(
        30), border_color=ft.Colors.AMBER, color=ft.Colors, label_style=ft.TextStyle(size=12), col={'xs': 12, 'sm': 2})

    nome_m2 = ft.TextField(label='Nome do Motorista', width=200, height=30, text_size=12, border_radius=ft.border_radius.all(
        30), border_color=ft.Colors.AMBER, color=ft.Colors, label_style=ft.TextStyle(size=12), col={'xs': 12, 'sm': 2})

    horario2 = ft.TextField(label='Horario de Saída', width=200, height=30, text_size=12, border_radius=ft.border_radius.all(
        30), border_color=ft.Colors.AMBER, color=ft.Colors.WHITE, label_style=ft.TextStyle(size=12), col={'xs': 12, 'sm': 2})

    data_2 = ft.TextField(label='Data', width=200, height=30, text_size=12, border_radius=ft.border_radius.all(
        30), border_color=ft.Colors.AMBER, color=ft.Colors.WHITE, label_style=ft.TextStyle(size=12), col={'xs': 12, 'sm': 2})

    def atualizar_prancheta2():

        page.clean()

        def fechar(e):
            atualizado.content.controls.clear()
            page.add(p)
            page.update

        def salvar(e):
            nome = nome_f2.value
            linha = linha_p2.value
            vaga = vaga_m2.value
            nome2 = nome_m2.value
            horario_2 = horario2.value
            data = data_2.value
            cadastrar_prancheta2(nome, linha, vaga, nome2, horario_2, data)
            atualizar_prancheta2()

        def deletar(e):
            selected_row = [
                linha for linha in row5.content.controls[0].rows if linha.selected
            ]

            if not selected_row:
                page.open(ft.SnackBar(ft.Text('Nenhum item selecionado!')))

            selected_cell = selected_row[0].cells[0].content.value

            try:
                conexao = conectar_db()
                cursor = conexao.cursor()

                cursor.execute(
                    'delete from prancheta2_rasa where id=%s', (selected_cell,))
                cursor.fetchall()
                conexao.commit()

                cursor.close()
                conexao.close()

                page.open(ft.SnackBar(ft.Text('Item deletado com Sucesso!!')))
                atualizar_prancheta2()

            except:
                page.open(ft.SnackBar(ft.Text('Algo eu Errado!!')))
        global dado_prancheta2
        dado_prancheta2 = atualizar_rasaXcentro()
        row5 = ft.Container(
            content=ft.ResponsiveRow(
                controls=[
                    ft.DataTable(
                        columns=[
                            ft.DataColumn(label=ft.Text(
                                'Id', col={'xs': 12, 'sm': 1}, size=10), heading_row_alignment=ft.MainAxisAlignment.START),
                            ft.DataColumn(label=ft.Text(
                                'Nome do Fiscal', col={'xs': 12, 'sm': 1}, size=10), heading_row_alignment=ft.MainAxisAlignment.START),
                            ft.DataColumn(
                                label=ft.Text('Linha Principal', col={'xs': 12, 'sm': 1}, size=10), heading_row_alignment=ft.MainAxisAlignment.START),
                            ft.DataColumn(label=ft.Text(
                                'Vaga', col={'xs': 12, 'sm': 1}, size=10), heading_row_alignment=ft.MainAxisAlignment.START),
                            ft.DataColumn(label=ft.Text(
                                'Nome do Motorista', col={'xs': 12, 'sm': 1}, size=10), heading_row_alignment=ft.MainAxisAlignment.START),
                            ft.DataColumn(label=ft.Text(
                                'Horario de Saída', col={'xs': 12, 'sm': 1}, size=10), heading_row_alignment=ft.MainAxisAlignment.START),
                            ft.DataColumn(label=ft.Text(
                                'Data', col={'xs': 12, 'sm': 1}, size=10), heading_row_alignment=ft.MainAxisAlignment.START)
                        ],
                        rows=[
                            ft.DataRow(
                                cells=[
                                    ft.DataCell(content=ft.Text(
                                        id, col={'xs': 12, 'sm': 1}, size=10)),
                                    ft.DataCell(content=ft.Text(
                                        nome, col={'xs': 12, 'sm': 1}, size=10)),
                                    ft.DataCell(content=ft.Text(
                                        linha, col={'xs': 12, 'sm': 1}, size=10)),
                                    ft.DataCell(content=ft.Text(
                                        vaga, col={'xs': 12, 'sm': 1}, size=10)),
                                    ft.DataCell(content=ft.Text(
                                        nome_m_2, col={'xs': 12, 'sm': 1}, size=10)),
                                    ft.DataCell(
                                        content=ft.Text(horario_2, col={'xs': 12, 'sm': 1}, size=10)),
                                    ft.DataCell(content=ft.Text(
                                        data_2, col={'xs': 12, 'sm': 1}, size=10))
                                ],
                                selected=False,
                                on_select_changed=toggle_select,
                                data=0
                            )for id, nome, linha, vaga, nome_m_2, horario_2, data_2 in dado_prancheta2
                        ],
                        divider_thickness=1,
                        vertical_lines=ft.BorderSide(
                            width=2, color=ft.Colors.AMBER),
                        horizontal_lines=ft.BorderSide(
                            width=2, color=ft.Colors.AMBER),
                        border=ft.border.all(
                            width=2, color=ft.Colors.AMBER),
                        border_radius=ft.border_radius.all(5),
                        # data_row_color=ft.Colors.GREY,
                        heading_row_color=ft.Colors.BLUE_900,
                        column_spacing=10




                    )
                ]


            )

        )

        atualizado = ft.Container(
            content=ft.ResponsiveRow(
                controls=[
                    ft.ResponsiveRow(
                        controls=[
                            ft.ElevatedButton(
                                "Prancheta Rasa X Centro", bgcolor=ft.Colors.AMBER, color=ft.Colors.BLACK, width=250, col={'xs': 4, 'sm': 3}, style=ft.ButtonStyle(text_style=ft.TextStyle(size=12, weight=ft.FontWeight.BOLD))),
                            ft.ElevatedButton(text='Cadastrar',
                                              bgcolor=ft.Colors.GREEN, color=ft.Colors.BLACK, width=100, on_click=salvar, col={'xs': 3, 'sm': 3}, style=ft.ButtonStyle(text_style=ft.TextStyle(size=12, weight=ft.FontWeight.BOLD))),
                            ft.ElevatedButton(text='Deletar', color=ft.Colors.BLACK,
                                              bgcolor=ft.Colors.RED, width=100, on_click=deletar, col={'xs': 3, 'sm': 3}, style=ft.ButtonStyle(text_style=ft.TextStyle(size=12, weight=ft.FontWeight.BOLD))),
                            ft.Container(col={'xs': 0, 'sm': 2}),

                            ft.IconButton(icon=ft.Icons.CLOSE,
                                          icon_color=ft.Colors.RED, on_click=fechar, col={'xs': 1, 'sm': 1}, style=ft.ButtonStyle(text_style=ft.TextStyle(size=12, weight=ft.FontWeight.BOLD)))
                        ]
                    ),
                    ft.Container(
                        content=ft.ResponsiveRow(
                            controls=[
                                nome_f2,
                                linha_p2,
                                vaga_m2,
                                nome_m2,
                                horario2,
                                data_2
                            ]
                        )
                    ),
                    row5
                ]
            )
        )
        page.add(atualizado)
        page.update()

    def dt_prancheta2(e):
        atualizar_prancheta2()
    global p
    p = ft.Container(

        content=ft.Column(

            controls=[

                ft.Container(
                    content=ft.ResponsiveRow(
                        columns=12,
                        col={'xs': 12, 'sm': 4},
                        controls=[
                            ft.ElevatedButton(text='Informações Cooperados', on_click=dt_cooperados,
                                              bgcolor=ft.Colors.AMBER, color=ft.Colors.BLACK, width=200, style=ft.ButtonStyle(text_style=ft.TextStyle(size=12, weight=ft.FontWeight.BOLD)), col={'xs': 12, 'sm': 2}),

                            ft.ElevatedButton(text='Informações Mot/Auxiliar', on_click=dt_mot_aux,
                                              bgcolor=ft.Colors.AMBER, color=ft.Colors.BLACK, width=200, style=ft.ButtonStyle(text_style=ft.TextStyle(size=12, weight=ft.FontWeight.BOLD)), col={'xs': 12, 'sm': 2}),

                            ft.ElevatedButton(text='Informações Fiscais', on_click=dt_fiscais,
                                              bgcolor=ft.Colors.AMBER, color=ft.Colors.BLACK, width=200, style=ft.ButtonStyle(text_style=ft.TextStyle(size=12, weight=ft.FontWeight.BOLD)), col={'xs': 12, 'sm': 2}),
                            ft.ElevatedButton(text='Prancheta Vila Verde X Centro', on_click=dt_pranchetas1,
                                              bgcolor=ft.Colors.AMBER, color=ft.Colors.BLACK, width=200, style=ft.ButtonStyle(text_style=ft.TextStyle(size=12, weight=ft.FontWeight.BOLD)), col={'xs': 12, 'sm': 2}),
                            ft.ElevatedButton(text='Prancheta Rasa X Centro', on_click=dt_prancheta2,
                                              bgcolor=ft.Colors.AMBER, color=ft.Colors.BLACK, width=200, style=ft.ButtonStyle(text_style=ft.TextStyle(size=12, weight=ft.FontWeight.BOLD)), col={'xs': 12, 'sm': 2})
                        ]
                    )
                ),

                ft.ResponsiveRow(
                    controls=[
                        ft.Image(
                            src='https://buzios.rj.gov.br/wp-content/uploads/2021/09/WhatsApp-Image-2021-09-09-at-15.03.11.jpeg',
                            fit=ft.ImageFit.COVER,
                            expand=True,
                            height=None,
                            border_radius=ft.border_radius.all(30),
                            col={'xs': 12, 'sm': 12}
                        )

                    ]
                )



            ]
        )

    )
    page.add(p)


if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')
