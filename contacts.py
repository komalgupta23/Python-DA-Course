contacts = {
    'police' : '112',
    'ambulance' : '102'
    
}
print(contacts)
while True:
    print("🔍 Search a contact:")
    q = input('Enter:')
    if len(q) == 0:
        print('Closing Down...')
        break
    if q in contacts:
        print(f'✔ {q}: {contacts[q]}')
    elif q == 'all':
        print('All Contacts')    
        for k, v in contacts.items():
            print(f'✔ {k} : {v}')
    
    else:
        print(f'😕 {q} not found!')
        print('📝 Add a new contact?')
        new_contact = input('Enter: ')
        if len(new_contact) == 0:
            print('skipping...')
        contacts[q] = new_contact
        print(f'✔ {q}: {contacts[q]} added')
        
        