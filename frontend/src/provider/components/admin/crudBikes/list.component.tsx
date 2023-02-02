import DataTable from 'react-data-table-component';
import React from "react";

const List = ({ list }: any) => {
    const [selectedRows, setSelectedRows]: any = React.useState(false);
    const [toggledClearRows, setToggleClearRows] = React.useState(false);

    const handleChange = ({ selectedRows }: any) => {
        setSelectedRows(selectedRows);
    };

    const removeSelectedBikes = () => {
        console.log(selectedRows.id);
        // console.log(selectedRows);
        
        // if (selectedRows.length > 0) {
        //     // deleteBike(selectedRows)
        // }
        // setToggleClearRows(!toggledClearRows);
        // setSelectedRows([])
    };

    const columns = [
        {
            name: 'ID',
            selector: (row: any) => row.id,
            sortable: true
        },
        {
            name: 'Number',
            selector: (row: any) => row.number,
            sortable: true
        },
        {
            name: 'Warning',
            selector: (row: any) => <input type="checkbox" defaultChecked={row.warning} />,
            sortable: true
        },
        {
            name: 'Disabled',
            selector: (row: any) => <input type="checkbox" defaultChecked={row.disabled} />,
            sortable: true
        },
    ];


    return (
        <div>
            <button type='button' onClick={() => {
                    removeSelectedBikes()
                }}>AAAA</button>
            {
                <DataTable
                    columns={columns}
                    data={list}
                    pagination
                    selectableRows
                    onSelectedRowsChange={handleChange}
                    clearSelectedRows={toggledClearRows}

                />
            }
        </div>
    );
}

export default List;