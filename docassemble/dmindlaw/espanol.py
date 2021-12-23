import docassemble.base.functions
from docassemble.base.util import capitalize

__all__ = []

male = {
  '0': 'zeroth',
  '1': 'primero',
  '2': 'segundo',
  '3': 'tercero',
  '4': 'cuarto',
  '5': 'quinto',
  '6': 'sexto',
  '7': 'séptimo',
  '8': 'octavo',
  '9': 'noveno',
  '10': 'décimo'
}

female = {
  '0': 'zeroth',
  '1': 'primera',
  '2': 'segunda',
  '3': 'tercera',
  '4': 'cuarta',
  '5': 'quinta',
  '6': 'sexta',
  '7': 'séptima',
  '8': 'octava',
  '9': 'novena',
  '10': 'décima'
}

def ordinal_es(the_number, **kwargs):
  the_number = str(the_number).strip()
  gender = kwargs.get('gender', 'male')
  output = None
  if gender == 'female':
    if the_number in female:
      output = female[the_number]
  else:
    if the_number in male:
      output = male[the_number]
  if output is None:
    output = the_number + ('a' if gender == 'female' else 'o')
  if kwargs.get('capitalize', False):
    output = capitalize(output)
  return output

docassemble.base.functions.update_language_function('es', 'ordinal', ordinal_es)