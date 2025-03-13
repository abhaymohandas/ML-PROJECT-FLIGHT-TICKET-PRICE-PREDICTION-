import streamlit as st
from PIL import Image
import pickle
import pandas as pd
import numpy as np

def pred():
    # Set the background image using custom CSS
    st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('https://images.unsplash.com/photo-1506012787146-f92b2d7d6d96?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wxMjA3fDB8MXxzZWFyY2h8MTV8fCUyMmFpcnBsYW5lJTIwdHJhdmVsJTIyfGVufDB8MHx8fDE3MjIyNTAyODN8Mg&ixlib=rb-4.0.3&q=80&w=1080');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        min-height: 100vh; /* Full viewport height */
    }
                
    /* Custom style for the title */
    h1 {
        color: #ffffff; /* White text color */
        font-size: 48px; /* Font size */
        text-shadow: 2px 2px 4px #000000; /* Shadow effect for better visibility */
        text-align: center; /* Center align the text */
        margin-top: 20px; /* Add some top margin */
    }

    /* Custom style for the header */
    h2 {
        color: #ffcc00; /* Yellow text color */
        font-size: 36px; /* Font size */
        text-shadow: 2px 2px 4px #000000; /* Shadow effect for better visibility */
        text-align: center; /* Center align the text */
        margin-top: 20px; /* Add some top margin */
    }
    
          
    </style>
    """, unsafe_allow_html=True)
    # Add your content or other Streamlit components here
    st.title("TICKET PRICE PREDICTION")
    st.header("ENTER THE DATA BELOW")

    # Call the pred function to render the content
    airline = st.selectbox('Select Your Airline', ['SpiceJet', 'AirAsia', 'Vistara', 'GO_FIRST', 'Indigo', 'Air_India'], index=None)
    st.write(f':red[You Have Selected airline: :green[{airline}]]')

    flight = st.selectbox('Select Your flight', [ 'SG-8709', 'SG-8157', 'I5-764', 'UK-995', 'UK-963', 'UK-945', 'UK-927', 'UK-951', 'G8-334', 'G8-336', 'G8-392', 'G8-338', '6E-5001', '6E-6202', '6E-549', '6E-6278', 'AI-887', 'AI-665', 'I5-747', 'G8-266', 'G8-101', 'G8-103', 'AI-441', '6E-5328', 'UK-933', '6E-2046', 'I5-744', 'SG-8169', '6E-5041', 'G8-165', '6E-2373', 'UK-813', 'UK-817', 'UK-819', 'UK-801', 'UK-815', 'AI-453', 'SG-2976', 'AI-504', 'AI-502', 'AI-506', 'AI-803', 'AI-479', 'SG-339', 'UK-955', 'UK-627', 'I5-784', 'AI-9643', 'AI-540', 'AI-429', 'AI-439', 'AI-9645', '6E-2193', '6E-2168', '6.00E-152', '6E-369', 'UK-899', 'AI-764', 'UK-747', 'UK-809', 'UK-737', '6E-2338', 'G8-237', 'UK-871', 'AI-762', 'G8-1404', 'AI-512', 'AI-537', 'UK-977', '6.00E-184', 'SG-3002', '6E-2102', 'AI-801', 'UK-637', 'UK-835', 'AI-531', 'UK-705', 'UK-707', 'UK-673', 'AI-839', 'UK-879', 'G8-191', 'AI-767', 'AI-401', 'AI-473', 'G8-213', 'AI-409', 'UK-837', 'AI-877', 'SG-8803', 'UK-985', 'UK-953', 'G8-346', 'G8-330', 'G8-323', '6.00E-218', '6E-6722', 'AI-868', 'AI-805', 'AI-624', 'G8-188', 'AI-636', '6E-2022', 'AI-469', 'AI-542', 'AI-560', 'UK-683', 'AI-403', '6E-2154', 'AI-9843', 'AI-544', '6.00E-282', 'UK-859', 'UK-829', 'AI-9857', '6E-607', 'AI-885', 'SG-2277', 'G8-719', 'G8-119', 'G8-717', 'UK-706', 'AI-465', '6E-5018', 'UK-839', 'UK-833', 'AI-406', 'AI-9809', 'G8-286', 'UK-847', 'AI-411', 'G8-113', 'SG-8483', 'AI-475', '6.00E-181', '6E-2092', 'AI-9911', '6E-5063', '6E-7403', 'UK-855', 'AI-807', 'G8-300', 'AI-811', 'AI-431', 'SG-1089', 'SG-1061', 'SG-1063', '6E-2054', 'AI-678', 'G8-1010', 'AI-435', 'AI-499', 'AI-9887', 'AI-483', 'G8-357', 'AI-451', 'AI-471', 'SG-1091', 'UK-981', 'UK-975', 'UK-993', 'UK-943', 'UK-941', 'I5-721', 'I5-773', 'G8-199', 'SG-8339', 'AI-481', 'AI-9939', 'UK-811', 'UK-807', 'AI-9915', '6E-2137', '6E-2097', '6E-926', 'AI-415', 'G8-2401', 'UK-727', 'AI-423', 'AI-865', '6E-2083', 'AI-485', '6E-5088', 'I5-740', 'I5-482', '6E-2901', '6E-6261', '6E-2013', 'I5-1529', 'I5-741', 'G8-7533', 'G8-7534', 'G8-7535', 'G8-530', 'G8-354', 'G8-2501', '6.00E-171', 'I5-788', 'G8-211', 'G8-7553', 'G8-2509', 'G8-194', 'G8-2609', '6E-2042', 'G8-713', 'I5-798', 'I5-775', 'G8-7541', 'G8-2403', 'G8-203', 'G8-209', 'AI-837', 'I5-881', '6E-5329', '6E-2081', '6E-573', 'AI-491', 'AI-883', 'AI-9609', 'AI-9015', 'SG-9974', 'AI-9017', '6E-865', 'I5-735', '6E-2033', '6E-6245', '6E-5042', 'SG-8723', 'SG-8701', '6E-2519', '6.00E-153', '6E-5026', '6E-5087', '6E-736', 'AI-861', '6E-6939', '6E-6231', 'AI-437', '6.00E-212', '6E-7336', '6E-6098', '6E-698', 'UK-812', 'AI-641', 'SG-2643', 'G8-268', 'G8-207', 'G8-404', '6E-7348', '6E-2274', 'G8-105', 'G8-2511', 'G8-143', '6E-2176', '6E-864', 'G8-108', 'AI-407', 'AI-487', 'G8-107', 'UK-671', 'SG-191', '6E-2026', '6E-5175', '6E-2188', '6E-654', '6E-2028', 'I5-548', 'SG-8185', 'SG-8946', '6E-2471', '6.00E-186', 'G8-2513', 'G8-131', '6E-2147', '6.00E-198', 'G8-133', '6E-6205', '6E-2247', '6E-2005', 'I5-767', 'I5-792', 'I5-783', 'AI-459', 'UK-741', 'AI-467', 'SG-143', '6E-2914', '6E-788', '6E-2616', '6E-2336', '6E-2131', 'I5-710', 'I5-711', 'SG-8938', 'I5-768', 'G8-171', '6.00E-221', 'SG-8721', '6E-2331', 'SG-8645', 'SG-8171', 'SG-8411', 'SG-8207', 'G8-173', 'I5-779', '6E-2769', '6E-5059', '6E-7407', 'I5-787', 'SG-5007', 'SG-6001', 'SG-534', '6E-2036', 'I5-550', 'SG-5012', 'SG-8941', '6E-772', '6E-967', '6E-2753', 'UK-721', 'I5-791', 'SG-8910', 'I5-713', 'G8-275', 'G8-422', 'I5-559', 'G8-7549', 'G8-231', '6E-2343', 'G8-7555', 'G8-145', '6E-2478', '6E-2348', '6E-2082', '6E-6233', '6E-2249', 'G8-7542', 'SG-480', '6E-552', '6E-951', '6.00E-286', '6E-6264', '6.00E-177', '6E-767', '6E-5014', 'G8-1171', 'SG-8191', '6E-2048', '6E-6612', '6.00E-308', '6E-781', 'SG-8905', '6E-6565', '6E-2015', 'SG-197', '6E-963', 'SG-389', 'AI-889', 'SG-946', 'SG-8480', 'G8-2201', '6E-353', '6E-483', '6E-2106', 'SG-8253', '6E-912', '6E-2057', '6E-6238', '6E-2485', '6E-6271', '6E-2513', '6E-755', '6E-2615', '6E-397', 'SG-8903', 'SG-8187', 'UK-641', '6E-6195', 'G8-153', 'AI-891', '6E-2178', '6E-2032', '6E-2181', '6E-6971', '6E-5031', 'AI-879', '6E-5073', 'SG-8152', '6E-2089', '6E-2329', 'SG-8106', '6E-2148', 'SG-8263', '6E-2367', '6E-2001', '6E-398', '6E-889', '6E-761', '6E-5012', '6E-6187', '6E-2043', '6E-5336', '6E-2031', '6E-2841', '6E-387', 'AI-9991', '6E-6171', 'AI-895', '6E-5003', '6E-358', '6E-6613', 'AI-489', '6E-2109', '6E-2517', '6E-6636', '6.00E-128', 'SG-1072', '6.00E-148', 'G8-423', 'I5-829', 'SG-1074', '6.00E-251', 'I5-737', '6E-5037', '6E-6096', '6E-6186', '6E-2087', '6E-6198', '6E-5016', '6.00E-307', '6E-947', '6E-2016', 'SG-263', 'SG-292', '6E-546', '6E-972', '6E-6197', '6E-5071', 'G8-151', '6E-6282', 'SG-8195', '6E-2843', '6E-2479', 'SG-958', 'AI-493', 'SG-6027', '6E-2938', '6E-2939', '6E-2346', '6E-2076', '6E-2618', '6E-2107', '6E-943', '6E-6023', '6E-6189', '6E-635', 'SG-8968', 'SG-8107', '6.00E-289', '6E-2162', '6E-2169', '6E-2061', 'SG-1071', 'SG-1056', '6E-954', '6E-6739', 'SG-8193', 'SG-8913', 'SG-8103', 'SG-107', '6E-2719', 'UK-994', 'UK-910', 'G8-339', '6E-6004', '6E-2077', 'AI-888', 'AI-867', 'AI-660', 'G8-351', 'AI-442', 'UK-958', 'UK-960', 'SG-8710', 'SG-8158', 'I5-942', '6E-416', 'UK-940', 'UK-944', '6E-939', '6.00E-168', 'AI-631', 'I5-631', 'UK-996', '6E-5382', '6E-6201', '6.00E-176', '6E-6222', 'AI-639', 'AI-649', 'UK-988', 'UK-651', 'UK-863', 'AI-675', '6E-6234', 'G8-287', 'UK-851', 'AI-651', 'SG-4417', 'UK-613', 'UK-875', 'UK-852', '6E-574', 'AI-611', 'UK-853', 'G8-349', 'SG-349', 'UK-773', '6E-5384', '6E-5392', 'UK-771', 'UK-825', 'AI-673', 'AI-9657', 'AI-681', 'UK-775', 'G8-329', 'G8-327', 'G8-319', 'G8-322', '6E-6721', 'AI-806', 'AI-809', '6E-5372', 'G8-365', 'G8-387', 'G8-520', 'G8-511', 'AI-635', '6E-2047', 'SG-2697', 'UK-970', 'SG-8702', 'UK-928', 'G8-364', 'SG-276', 'AI-774', 'AI-619', 'AI-643', 'UK-823', 'AI-667', 'UK-621', 'UK-865', 'AI-685', 'UK-841', 'AI-683', 'G8-382', 'AI-625', 'G8-575', 'G8-331', '6E-2172', '6E-5017', 'AI-687', 'G8-391', 'UK-877', '6.00E-213', 'AI-627', 'UK-655', 'AI-637', 'AI-655', 'AI-607', 'G8-383', 'AI-645', 'AI-663', 'AI-570', 'G8-381', 'AI-671', 'G8-2440', 'SG-1092', 'SG-1090', 'SG-1062', 'I5-620', 'G8-2502', 'SG-343', 'AI-688', 'AI-629', 'AI-669', 'AI-9919', 'AI-679', 'SG-1059', 'UK-954', 'UK-930', 'UK-986', 'UK-950', 'UK-902', 'G8-461', 'UK-653', 'UK-873', 'UK-849', 'UK-845', 'UK-857', 'G8-317', 'UK-821', 'UK-827', '6E-2518', '6E-5386', '6.00E-296', 'AI-864', '6E-6182', 'I5-330', 'I5-1569', '6.00E-248', '6E-5395', 'UK-861', 'I5-471', 'G8-7536', 'G8-7537', 'G8-7538', 'G8-341', 'G8-345', 'G8-321', 'G8-2508', '6E-5013', 'I5-678', 'I5-336', 'G8-244', 'G8-2417', 'G8-7546', 'G8-306', 'G8-7545', 'G8-371', 'G8-2411', 'G8-363', '6E-5376', 'G8-325', 'G8-2606', '6E-5006', '6.00E-154', '6E-945', 'AI-615', 'AI-695', 'AI-657', 'AI-633', 'I5-941', 'AI-652', '6E-5361', 'SG-8179', '6E-5308', '6E-5047', 'I5-338', '6E-6515', '6E-6993', '6E-5313', '6E-6084', '6.00E-164', '6E-5381', '6E-5332', '6.00E-138', '6E-2103', '6E-439', '6E-5501', '6E-821', 'AI-623', '6E-6029', 'SG-223', 'AI-601', 'G8-398', 'G8-3184', '6E-5431', 'G8-2504', 'G8-2506', 'AI-603', '6E-5338', '6E-5366', '6.00E-219', '6E-6463', '6E-6258', '6E-354', '6E-5209', '6E-5312', '6.00E-236', '6E-5217', '6E-5359', '6E-6109', '6E-5391', 'I5-423', 'SG-455', '6.00E-179', 'SG-488', '6E-5307', '6E-5317', 'G8-390', '6E-5396', '6E-5202', 'SG-475', '6E-331', '6E-6818', '6E-5375', '6E-5208', '6E-6123', '6.00E-136', '6E-5393', '6E-6051', '6E-711', '6E-5316', '6E-5236', 'G8-2601', 'G8-602', 'G8-7561', 'SG-9923', '6E-5371', '6E-7292', '6E-6809', '6E-825', '6E-5352', '6E-6478', '6E-6817', '6E-6293', '6E-5345', '6E-739', 'SG-415', 'SG-634', '6E-461', '6.00E-234', '6E-818', '6E-448', '6E-434', '6E-6094', '6E-5337', '6E-907', 'G8-705', '6E-5343', 'SG-3440', '6E-395', '6E-6014', '6E-6749', 'SG-467', '6E-6326', '6.00E-205', '6E-5342', '6E-363', 'SG-241', '6E-312', '6E-5302', 'SG-401', 'SG-163', 'SG-251', '6E-544', 'SG-923', '6E-519', '6E-5373', 'SG-611', '6E-5349', '6E-6088', '6E-6475', '6E-559', 'SG-5018', '6E-832', '6E-627', 'SG-5074', 'G8-2605', '6E-6474', '6.00E-227', '6E-6223', 'SG-5079', '6E-6086', '6E-5355', '6E-533', '6E-542', '6E-802', 'SG-487', 'G8-397', 'G8-2607', 'SG-3248', '6E-932', 'G8-7557', 'G8-347', 'G8-305', 'G8-384', '6E-5206', '6E-6206', '6E-5214', '6E-5368', '6E-5379', '6E-5398', 'SG-6003', 'SG-5019', 'G8-303', 'AI-9030', '6E-6292', '6E-911', 'I5-996', 'UK-820', 'UK-802', '6E-6139', '6E-2514', '6E-2027', '6E-2174', '6E-2034', 'AI-505', 'AI-501', 'AI-503', 'I5-1566', 'G8-405', 'G8-873', 'G8-385', 'SG-136', 'I5-1528', '6E-2186', 'AI-804', 'UK-810', 'AI-808', 'I5-749', 'AI-523', 'UK-808', 'UK-816', 'UK-818', 'I5-1982', 'I5-1426', 'UK-858', '6E-6104', 'I5-2392', 'AI-640', '6E-436', 'UK-657', 'G8-283', 'AI-573', '6E-6257', 'SG-4009', 'I5-592', 'SG-531', '6.00E-276', '6E-6753', 'UK-850', 'G8-395', '6E-484', '6E-6535', 'SG-209', '6E-415', '6E-6491', '6E-7223', 'UK-854', '6E-702', 'G8-320', '6E-886', 'I5-992', 'SG-3027', '6E-528', '6E-6067', 'I5-1229', 'AI-9501', 'AI-9517', 'G8-803', 'UK-755', 'SG-198', 'I5-892', 'I5-589', '6E-2337', '6E-455', '6E-807', '6E-6393', 'AI-507', 'AI-9876', '6E-6339', 'I5-1621', 'I5-819', 'G8-146', 'AI-9505', 'AI-9547', 'SG-768', 'G8-116', 'G8-118', 'I5-1782', 'G8-312', 'SG-4005', 'AI-9927', 'SG-517', 'SG-327', 'UK-867', '6E-6802', 'SG-3023', 'AI-565', 'SG-5013', 'SG-5002', 'SG-535', 'I5-410', 'I5-1780', 'I5-2472', 'G8-791', 'AI-516', 'AI-610', 'AI-748', 'AI-738', 'AI-9925', 'G8-285', 'UK-814', '6E-2025', '6E-6386', 'I5-972', 'UK-897', 'UK-893', 'UK-864', 'UK-846', 'UK-866', 'AI-9931', 'I5-5405', 'I5-5402', 'I5-1321', 'I5-722', '6E-855', '6E-638', '6E-426', 'I5-818', 'I5-1427', 'I5-991', 'I5-1561', 'I5-820', 'I5-2461', 'I5-1451', 'SG-5006', 'I5-1783', 'I5-1576', 'I5-1228', 'I5-1983', 'I5-1731', 'I5-1562', 'I5-339', 'G8-808', 'G8-7547', 'G8-7548', 'G8-241', 'G8-2231', 'G8-7543', 'G8-399', 'G8-518', '6E-747', 'G8-510', '6.00E-232', '6E-708', '6E-2053', 'SG-468', '6E-684', 'I5-1540', 'I5-1530', 'I5-334', '6E-543', '6E-6178', 'G8-294', 'G8-815', 'SG-516', '6E-6876', '6E-408', 'AI-776', 'SG-438', 'SG-635', '6E-469', '6E-537', '6E-869', '6E-6247', '6E-871', '6E-735', '6E-5007', 'SG-8906', 'G8-374', 'G8-401', 'G8-403', 'SG-3233', 'SG-3719', '6E-7257', 'SG-3725', 'AI-604', 'I5-736', 'AI-772', 'G8-292', 'AI-564', 'G8-805', 'G8-801', 'AI-583', '6.00E-113', '6E-5365', '6E-5323', '6.00E-131', '6E-7227', '6.00E-295', '6E-6345', '6.00E-161', '6E-5203', '6E-5389', '6E-841', '6E-541', 'I5-1622', '6E-6017', '6E-6445', '6E-5399', '6E-6517', 'SG-5072', '6E-379'],index=None)
    st.write(f':red[You Have Selected Your flight: :green[{flight}]]')


    source_city = st.selectbox('Select Your source_city:', ['Delhi', 'Mumbai', 'Bangalore', 'Kolkata', 'Hyderabad', 'Chennai'], index=None)
    st.write(f':red[You Have Selected source_city: :green[{source_city}]]')

    time = ['Evening', 'Early_Morning', 'Morning', 'Afternoon', 'Night', 'Late_Night']
    departure_time = st.radio('Select Your departure_time:', options=time, index=None)
    st.write(f':red[You Have Selected departure time: :green[{departure_time}]]')

    stops = st.selectbox('Select stops:', ['zero', 'one', 'two_or_more'], index=None)
    st.write(f':red[You Have Selected stops: :green[{stops}]]')

    destination_city = st.selectbox('Select Your destination city:', ['Mumbai', 'Bangalore', 'Kolkata', 'Hyderabad', 'Chennai', 'Delhi'], index=None)
    st.write(f':red[You Have Selected destination city: :green[{destination_city}]]')

    atime = ['Evening', 'Early_Morning', 'Morning', 'Afternoon', 'Night', 'Late_Night']
    arrival_time = st.radio('Select Your arrival_time', options=atime, index=None)
    st.write(f':red[You Have Selected arrival_time: :green[{arrival_time}]]')

    classes = ['Economy', 'Business']
    class1 = st.radio('Select Your class:', options=classes, index=None)
    st.write(f':red[You Have Selected class: :green[{class1}]]')

    def is_valid_duration(duration):
        try:
            float(duration)
            return True
        except ValueError:
            return False

    label = 'Enter Duration:'
    duration = st.text_input(label)
    if duration and is_valid_duration(duration):
        st.write(f':red[You Have Entered Duration: :green[{duration}]]')
    else:
        st.error('Please enter a valid number for duration.')

    def is_valid_day(day):
        try:
            int(day)
            return True
        except ValueError:
            return False

    label = 'Enter days left:'
    days_left = st.text_input(label)
    if days_left and is_valid_day(days_left):
        st.write(f':red[You Have days left: :green[{days_left}]]')
    else:
        st.error('Please enter a valid number for days left.')

    # Check if all inputs are provided
    if st.button('PREDICT'):
        if None in [airline, flight, source_city, departure_time, stops, destination_city, arrival_time, class1] or not duration or not days_left:
            st.warning("⚠️ You must fill in all inputs before predicting!")
        else:
            # Create the feature DataFrame
            features = pd.DataFrame([[flight, class1, duration, days_left, airline, source_city, departure_time, stops, arrival_time, destination_city]],
                                    columns=['flight', 'class1', 'duration', 'days_left', 'airline', 'source_city', 'departure_time', 'stops', 'arrival_time', 'destination_city'])

            # Load the saved models and transformers
            one1 = pickle.load(open('airline.sav', 'rb'))
            one2 = pickle.load(open('source_city.sav', 'rb'))
            one3 = pickle.load(open('departire_time.sav', 'rb'))
            one4 = pickle.load(open('stop.sav', 'rb'))
            one5 = pickle.load(open('arrival_time.sav', 'rb'))
            one6 = pickle.load(open('destination_city.sav', 'rb'))
            la1 = pickle.load(open('flight.sav', 'rb'))
            la2 = pickle.load(open('class1.sav', 'rb'))
            model = pickle.load(open('model.sav', 'rb'))
            scale = pickle.load(open('scale.sav', 'rb'))

            # Transform categorical features
            one1_output = one1.transform(features[['airline']])
            one2_output = one2.transform(features[['source_city']])
            one3_output = one3.transform(features[['departure_time']])
            one4_output = one4.transform(features[['stops']])
            one5_output = one5.transform(features[['arrival_time']])
            one6_output = one6.transform(features[['destination_city']])

            # Encode 'class1' and 'flight'
            features['class1'] = la2.transform(features['class1'])
            features['flight'] = la1.transform(features['flight'])

            # Concatenate transformed features
            new_airline = pd.DataFrame(one1_output, columns=one1.get_feature_names_out())
            features = pd.concat([features, new_airline], axis=1)
            features.drop('airline', axis=1, inplace=True)

            new_source_city = pd.DataFrame(one2_output, columns=one2.get_feature_names_out())
            features = pd.concat([features, new_source_city], axis=1)
            features.drop('source_city', axis=1, inplace=True)

            new_departure_time = pd.DataFrame(one3_output, columns=one3.get_feature_names_out())
            features = pd.concat([features, new_departure_time], axis=1)
            features.drop('departure_time', axis=1, inplace=True)

            new_stops = pd.DataFrame(one4_output, columns=one4.get_feature_names_out())
            features = pd.concat([features, new_stops], axis=1)
            features.drop('stops', axis=1, inplace=True)

            new_arrival_time = pd.DataFrame(one5_output, columns=one5.get_feature_names_out())
            features = pd.concat([features, new_arrival_time], axis=1)
            features.drop('arrival_time', axis=1, inplace=True)

            new_destination_city = pd.DataFrame(one6_output, columns=one6.get_feature_names_out())
            features = pd.concat([features, new_destination_city], axis=1)
            features.drop('destination_city', axis=1, inplace=True)

            # Scale the features and make predictions
            features = scale.transform(features)
            prediction = model.predict(features)
            st.write(f'YOUR ESTIMATED TICKET PRICE IS: :green[₹{prediction[0]:,.2f}]')

pred()