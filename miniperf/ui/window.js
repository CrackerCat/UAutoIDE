import React from 'react'
import { VscTools } from 'react-icons/vsc';
import { FcOpenedFolder } from 'react-icons/fc';
import { IconContext, DiJoomla } from 'react-icons';
import { Button, ButtonGroup, Form, Table, Navbar, Nav, FormControl, NavDropdown, OverlayTrigger, Tooltip, Modal, Row, Col } from 'react-bootstrap'

class Window extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            recording: false,
            exePath: "",
            symbolPaths: "http://xsjsymbol.testplus.cn;http://127.0.0.1:80",
            outputInfo: [],
            tables: [],
            settingDialogShow: false,
            curStatus: "",
            settingPath: {} // setting弹窗渲染的配置
        }
    }

    componentDidMount() {
        window.addEventListener("message", this.onMessage);
        window.addEventListener('pywebviewready', function() {
            window.pywebview.api.pywebviewready();
        })        
    }

    componentWillUnmount() {
        window.removeEventListener("message", this.onMessage);
    }

    onMessage(event) {
        let data = event.data;
        console.log("onMessage", data)
        if (data.type == "on_message") {
            data = data.data
            if (data.type == "notice" && data.msg == "stop") {
                this.setState({
                    recording: false
                })
            } else if (data.type == "out") {
                let outputInfo
                outputInfo = this.state.outputInfo
                outputInfo.push(data.msg)
                this.setState({
                    outputInfo: outputInfo
                })
            }
        }
    }


    render() {

        const renderTooltip = (props) => (
            <Tooltip id="button-tooltip" {...props}>
                Simple tooltip
            </Tooltip>
        );        

        return (
            <div>
                <Navbar bg="primary" variant="dark">
                    <Navbar.Brand href="#home">
                        <IconContext.Provider value={{ size: "2em" }}>
                            <VscTools />
                        </IconContext.Provider>

                    </Navbar.Brand>
                    <Nav className="mr-auto nav nav-tabs">
                        <Nav.Link onClick={() => window.pywebview.api.on_HomeClick() } autoFocus={true} href="#home" data-toggle="tab">Home</Nav.Link>                        
                    </Nav>
                    <Form inline>
                        <FormControl type="text" placeholder="Search" className="mr-sm-2" />
                        {/* <Button variant="outline-light">Search</Button> */}
                    </Form>
                    <Button variant="primary" onClick={() => this.on_GetFileList()} >刷新</Button>
                </Navbar>

                <br />
                <Table striped bordered hover>
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>表格名称</th>
                            <th>策划使用</th>
                            <th>程序使用</th>
                        </tr>
                    </thead>
                    <tbody>
                        {this.state.tables.map((value, index) => {
                            return (
                                <tr key={index}>
                                    <td>{index}</td>
                                    <td>{value.name}</td>
                                    <td>
                                        <ButtonGroup aria-label="Basic example">
                                            <OverlayTrigger placement="right" delay={{ show: 250, hide: 400 }} overlay={renderTooltip} >
                                                <Button variant="success" id={index} onClick={() => this.on_CheckTableClick(index)} >检正确性</Button>
                                            </OverlayTrigger>
                                            <Button variant="primary" onClick={() => this.on_GenTabFileClick(index)} >生成.csv</Button>
                                        </ButtonGroup>
                                    </td>
                                    <td>
                                        <ButtonGroup aria-label="Basic example">
                                            <Button variant="primary" onClick={() => this.on_GenCSAndTabCodeClick(index)} >生成.CS/.csv</Button>
                                        </ButtonGroup>
                                    </td>
                                </tr>
                            )
                        })}
                    </tbody>
                </Table>

                <Modal show={this.state.settingDialogShow} centered={true} size='lg' onHide={() => this.onChangeSettingDialog(false)} >
                    <Modal.Header closeButton>
                        <Modal.Title id="example-custom-modal-styling-title">
                            Settings
                    </Modal.Title>
                    </Modal.Header>
                    <Modal.Body>
                        <Form>
                            {
                                Object.keys(this.state.settingPath).map((item, index) => (
                                    <Form.Group as={Row} controlId="formHorizontalEmail" key={`${item}_${index}`}>
                                        <Form.Label column sm={2}>
                                            {item}
                                        </Form.Label>
                                        <Col sm={9}>
                                            <Form.Control placeholder={item} value={this.state.settingPath[item]} onChange={(e) => this.handleInputChange(e, item)} />
                                        </Col>
                                        <Col sm={1}>
                                            <IconContext.Provider value={{ size: "25px", style: { cursor: 'pointer' } }}>
                                                <FcOpenedFolder onClick={() => this.onFolderChange(item)} />
                                            </IconContext.Provider>
                                        </Col>
                                    </Form.Group>
                                ))
                            }
                        </Form>
                    </Modal.Body>
                    <Modal.Footer>
                        <Button variant="secondary" onClick={() => this.onChangeSettingDialog(false)}> Close </Button>
                        <Button variant="primary" onClick={() => this.saveSettings()} >Save changes</Button>
                    </Modal.Footer>
                </Modal>
            </div>
        )
    }
}

export default Window