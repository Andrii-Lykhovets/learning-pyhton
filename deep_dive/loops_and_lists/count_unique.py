def analyse_transport(list_of_records):
    all_transport_records = []
    unique_transport_records = []
    known_transport_records = ['car', 'bus', 'train', 'plane', 'bicycle']

    for record in list_of_records:
        if record in known_transport_records:
            all_transport_records.append(record)
            if record not in unique_transport_records:
                unique_transport_records.append(record)

    print('All transport:')
    print(all_transport_records)
    print('Unique transport(' + str(len(unique_transport_records)) + '):')
    print(unique_transport_records)


records = ['car', 'bus', 'pen', 'bottle', 'train', 'chair', 'car', 'car', 'table', 'bicycle']
analyse_transport(records)
