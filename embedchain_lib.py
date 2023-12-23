import os
from embedchain import App

def prescrizione_final_answer(bot, initial_answer):
  follow_up_query = ("Considerando che" + initial_answer + " e che sei un medico con anni di esperienza: "
                     "tieni conto della patologia sospetta e secondo le buone pratiche. "
                     "Rispondi con il nome del paziente e della patologia sospetta e dimmi se gli esami prescritti sono corretti. "
                     "Per essere assolutamente sicuri circa la patologia consiglia ulteriori indagini da fare indicandole chiaramente. "
                     "Nella risposta non includere che sei un medico. Rispondi sempre in italiano. "
                     "Se non puoi rispondere a domande, rispondi con 'Non riesco a leggere il file'.")
  return bot.query(follow_up_query)


#relative_path = "pdfs/Giuseppe Verdi- Dislipidemia.pdf"
relative_path = "pdfs/Mario Rossi - Diabete.pdf"
absolute_path = os.path.abspath(relative_path)
#print(f"The absolute path to 'analisi1.pdf' is {absolute_path}")

# Check if the PDF file exists at the specified absolute path
#if not os.path.isfile(absolute_path):
    #raise FileNotFoundError(f"The file {absolute_path} was not found.")

with st.spinner("Elaborazione in corso..."):
  medical_bot = App()
  
  medical_bot.add("pdf_file", absolute_path) # Il path assoluto è corretto e quindi posso usare il metodo add con il file pdf
  
  input_query = "Di cosa parla il file?"
    
  answer = medical_bot.query(input_query)
  
  final_answer = prescrizione_final_answer(medical_bot, answer)
  
  print(f"\nRisposta: {final_answer}\n\n")
