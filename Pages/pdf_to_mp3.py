#!/usr/bin/python3

# Блок выполнения конвертации pdf в mp3 формат
pdf = html.Div([
    html.Label("Введите или вставте путь к файлу .pdf", style={'color': 'green','display':'inline-block','padding': 10})
])

#pdf_to_mp3.main()

primer = html.Div([
    html.Div('Example Div', style={'color': 'blue', 'fontSize': 14}),
    html.P('Example P', className='my-class', id='my-p-element')
], style={'marginBottom': 100, 'marginTop': 25})

dop = html.Div([
    html.Br(),
    html.Label("Дополнительно:", style={'color': 'green','padding': 10}),
])
pdf = html.Div([
    dcc.Dropdown(options = ['PDF_TO_MP3', 'ПОИСК CTO'], 
        id = 'dropdown8', 
        value = 'Дополнительно',
        style = {'display':'inline-block','padding': 10, 'width': 135}),
    html.Form('Здесь будет текст', id = 'out2', style={'display':'inline-block','color': 'indigo','fontSize': 17, 'padding': 10})
    #html.Label("Введите или вставьте путь к файлу .pdf", style={'color': 'green','display':'inline-block','padding': 10})
])
#dopolneniy = 
